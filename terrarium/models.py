import time
import sys
sys.path.insert(1, '/usr/lib/python2.7/dist-packages/')
import smbus
from django import utils
from django.db import models
from main.models import KarniPiLog
from karnipi.i2c_helper import I2CValueAdapter


class Terrarium(models.Model):
    title = models.TextField()
    temperature_min = models.CharField(max_length=2)
    temperature_max = models.CharField(max_length=2)
    sunrise = models.TimeField()
    sunset = models.TimeField()
    sleep_mode = models.BooleanField(default=False)

    def __unicode__(self):
        return str(self.title)

    def sleep(self):
        self.sleep_mode = True
        self.save()

        for f in I2CActor.objects.all():
            f.off()

        log = KarniPiLog(type='INFO',
                         datetime=utils.timezone.now(),
                         message='Sleeping now...')
        log.save()

    def wake_up(self):
        self.sleep_mode = False
        self.save()

        bus = smbus.SMBus(1)  # Rev 2 Pi uses 1

        # reset port a
        bus.write_byte_data(0x20, 0x00, 0x00)

        # reset port b
        bus.write_byte_data(0x20, 0x01, 0x00)

        log = KarniPiLog(type='INFO',
                         datetime=utils.timezone.now(),
                         message='Waking up...')
        log.save()

    def is_sleeping(self):
        return self.sleep_mode

    def get_actors(self):
        return I2CActor.objects.all().filter(terrarium=self)

    def get_sensors(self):
        return I2CSensor.objects.all().filter(terrarium=self)


class I2CActor(models.Model):
    title = models.TextField()
    terrarium = models.ForeignKey(Terrarium)
    chip_address = models.CharField(max_length=2)
    data_address = models.CharField(max_length=2)
    value_address = models.CharField(max_length=2)
    state = models.BooleanField(default=False)

    def on(self):

        print "'{0}' ({3} {4} {5}): state change ({1} -> {2}) Address is {3} {4} {5}".format(self.title,
                                                                                         self.state,
                                                                                         True,
                                                                                         self.chip_address,
                                                                                         self.data_address,
                                                                                         self.value_address)
        if self.state == 0:
            log = KarniPiLog(type='INFO',
                             datetime=utils.timezone.now(),
                             message='Turned on ' + self.title + ' ' + self.chip_address + ' ' + self.data_address + ' ' + self.value_address)
            log.save()

        self.state = 1
        self.save()

        print "{0} {1} {2}".format(self.chip_address, self.data_address, self.value_address)
        adapter = I2CValueAdapter(self.chip_address, self.data_address)
        adapter.set_state(self.value_address, 1)

    def off(self):

        print "'{0}' ({3} {4} {5}): state change ({1} -> {2}) Address is {3} {4} {5}".format(self.title,
                                                                                         self.state,
                                                                                         False,
                                                                                         self.chip_address,
                                                                                         self.data_address,
                                                                                         self.value_address)

        log = KarniPiLog(type='INFO',
                         datetime=utils.timezone.now(),
                         message='Turned off ' + self.title)
        log.save()

        self.state = 0
        self.save()

        adapter = I2CValueAdapter(self.chip_address, self.data_address)
        adapter.set_state(self.value_address, 0)


class Heater(I2CActor):

    def on(self):
        I2CActor.on(self)

    def off(self):
        I2CActor.off(self)


class Sprinkler(I2CActor):

    def on(self):
        I2CActor.on(self)

    def off(self):
        I2CActor.off(self)


class Fogger(I2CActor):

    def on(self):
        I2CActor.on(self)

    def off(self):
        I2CActor.off(self)


class Fan(I2CActor):

    def on(self):
        I2CActor.on(self)

    def off(self):
        I2CActor.off(self)


class Light(I2CActor):

    def on(self):
        I2CActor.on(self)

    def off(self):
        I2CActor.off(self)
    

class I2CSensor(models.Model):
    title = models.TextField()
    terrarium = models.ForeignKey(Terrarium)
    bank = models.CharField(max_length=2)
    address = models.CharField(max_length=4)


class SHT21Sensor(I2CSensor):
    sht21 = None

    @staticmethod
    def read_temperature():
        from karnipi.sht21 import SHT21

        with SHT21(0) as sht21:
            return sht21.read_temperature()

    @staticmethod
    def read_humidity():
        from karnipi.sht21 import SHT21
        
        with SHT21(0) as sht21:
            return sht21.read_humidity()


class TerrariumLog(models.Model):
    time = models.DateTimeField()
    light = models.BooleanField(default=False)
    temperature = models.IntegerField()
    humidity = models.IntegerField()