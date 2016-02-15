
import sys
sys.path.append('/usr/lib/python2.7/dist-packages')
import smbus
from django import utils
from main.logger import KarniLogger
from main.models import KarniPiLog

class I2CValueAdapter():

    DEVICE = 0x20  # Device address (A0-A2)
    IODIRA = 0x00  # Pin direction register
    IODIRB = 0x01  # Pin direction register
    OLATA = 0x14  # Register for outputs
    GPIOA = 0x12  # Register for inputs

    bus = None
    chip_address = None
    data_address = None

    def __init__(self, chip_address, data_address):

        self.bus = smbus.SMBus(1)  # Rev 2 Pi uses 1

        print "Prepared SMBus"

        self.chip_address = 20

        if data_address == "14":
            self.data_address = 14
        elif data_address == "15":
            self.data_address = 15
        else:
            raise Exception('Invalid data address ' + data_address)

        KarniLogger().log_info("Initialized bus with chip address {0} and data address {1}".format(self.chip_address, self.data_address))
        KarniLogger().log_info("Checking current bus state...")
        self.get_state()

    @staticmethod
    def hex_to_binarystring(hex):
        scale = 16  ## equals to hexadecimal
        num_of_bits = 8
        return bin(int(str(hex), scale))[2:].zfill(num_of_bits)

    def get_state(self):

        try:
            if self.data_address == 14:
                retVal = self.bus.read_byte_data(0x20, 0x14)
                KarniLogger().log_info("bus read byte data = " + str(retVal))
                return retVal
            elif self.data_address == 15:
                retVal = self.bus.read_byte_data(0x20, 0x15)
                KarniLogger().log_info("bus read byte data = " + str(retVal))
                return retVal
            else:
                raise Exception
        except IOError as e:
            errno, strerror = e.args
            KarniLogger().log_info("I/O error({0}): {1}".format(errno,strerror))
            pass

    # set state of a specific device
    def set_state(self, value_address, state):

        KarniLogger().log_info("Setting state for value address {0} and state {1}".format(value_address, state))

        current_int = self.get_state()

        # get binary string of current bus state
        bus_binarystring = list(self.hex_to_binarystring(hex(current_int)))
        KarniLogger().log_info("Currently on bus = " + str(bus_binarystring))

        value_int = int(value_address)
        value_binarystring = list(self.hex_to_binarystring(hex(value_int)))
        KarniLogger().log_info("Value address    = " + str(value_binarystring))

        new_int = None

        # if device is switched on
        if str(state) == "1":
            new_int = int(value_address) | current_int
            KarniLogger().log_info("{0} XOR {1} = {2}".format(str(int(value_address)),
                                             str(current_int), new_int))
        # if device is switched off
        elif str(state) == "0":

            for i in range(len(bus_binarystring)):
                bus_bit = str(bus_binarystring[i])
                value_bit = str(value_binarystring[i])

                print "index = {0}, value = {1}, bus = {2}".format(i,
                                                                   value_bit,
                                                                   bus_bit)

                # if there are matching bits with value 1, set bus bit to 0
                if (bus_bit == "1") & (value_bit == "1"):
                    KarniLogger().log_debug("found mismatch at index " + str(i))
                    bus_binarystring[i] = "0"

            new_bus_binarystring = "".join(bus_binarystring)
            KarniLogger().log_info("New bus binary " + new_bus_binarystring)
            new_int = int(new_bus_binarystring, 2)
            KarniLogger().log_info("New bus int " + str (new_int))

        if str(self.data_address) == "14":
            self.bus.write_byte_data(0x20, self.IODIRA, 0x00)
        elif str(self.data_address) == "15":
            self.bus.write_byte_data(0x20, self.IODIRB, 0x00)
        else:
            KarniLogger().log_debug("PORT {0} unknown".format(str(self.data_address)))


        KarniLogger().log_info("Now working with {0} {1} {2}".format(self.chip_address,
                                                    self.data_address,
                                                    new_int))

        print type (self.data_address)
        if self.data_address == 14:
            self.bus.write_byte_data(0x20, 0x14, new_int)
        elif self.data_address == 15:
            self.bus.write_byte_data(0x20, 0x15, new_int)
        else:
            raise AttributeError("WTF")

        current_int = self.get_state()



