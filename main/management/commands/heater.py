import sys
import time

from django.core.management.base import NoArgsCommand

from terrarium.helper import TerrariumHelper
from main.logger import KarniLogger


class Command(NoArgsCommand):

    def handle_noargs(self, **options):

        control = KarniPiControl()

        # run as far as you can
        while True:
            exit_code = control.get_exit_code()
            KarniLogger().log_info("Checking for exit code..." + str(exit_code))

            if int(exit_code) == 0:
                KarniLogger().log_info("Staring next cycle...")

                try:
                    try:
                        terrarium = TerrariumHelper().get_terrarium()
                    except:
                        KarniLogger().log_info("Couldn't get terrarium...")

                    if terrarium.sleep_mode is False:
                        control.handle_control(terrarium)
                    else:
                        KarniLogger().log_info("Terrarium in sleep mode...exiting!")
                        sys.exit()

                except (KeyboardInterrupt, SystemExit):
                    KarniLogger().log_info("Exiting...")
                    sys.exit()
                finally:
                    KarniLogger().log_info("Idling for 10 minutes")
                    time.sleep(10*60)
            else:
                KarniLogger().log_info("Exiting due to exit code...")
                sys.exit()


class KarniPiControl():

    action = None

    def __init__(self):
        KarniLogger().log_info("Init control...")

    @staticmethod
    def get_exit_code():
        file_object = open('/home/pi/karnipi/main/daemons/exit.txt', 'r')
        sys_exit = file_object.read()
        file_object.close()
        return sys_exit

    def handle_control(self, terrarium):

        if self.action is None:
            self.action = "heating"

        KarniLogger().log_info("Getting terrarium data...")
        sht21 = TerrariumHelper().get_sht21_sensor(terrarium)
        print sht21
        temperature = int(sht21.read_temperature())
        print temperature
        # terra_data = TerrariumHelper().GetCurrentTerrariumData()

        KarniLogger().log_info("Accessing heater...")
        heater = TerrariumHelper().get_heater(terrarium)

        # if heater is available
        if heater is not None:
            KarniLogger().log_info("Terrarium: {0} C".format(int(temperature)))
            KarniLogger().log_info("Ziel-Temperatur: {0} C".format(int(terrarium.temperature_max)))
            KarniLogger().log_info("Action is '{0}'".format(self.action))

            if int(temperature) < int(terrarium.temperature_min):
                self.action = "heating"
                heater.on()
                KarniLogger().log_info("Heating...")
            elif (int(temperature) <= int(terrarium.temperature_max)) & (self.action == "heating"):
                heater.on()
            elif (int(temperature) <= int(terrarium.temperature_max)) & (self.action == "cool down"):
                heater.off()
            elif int(temperature) > int(terrarium.temperature_max):
                self.action = "cool down"
                heater.off()
                KarniLogger().log_info("Cooling down...")
            else:
                KarniLogger().log_info("Don't know what to do...")