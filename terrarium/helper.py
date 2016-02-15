#from __future__ import absolute_import

from django import utils

from config.helper import ConfigHelper
from terrarium.models import Terrarium, Fogger, Sprinkler, Fan, Light, Heater, TerrariumLog, SHT21Sensor


class TerrariumHelper():

    @staticmethod
    def GetTerrariumLog():
        return TerrariumLog.objects.order_by('-time')


    def GetCurrentTerrariumData(self):

        self.prevent_caching()

        latest_terrarium_data = TerrariumLog.objects.latest('time')
        return latest_terrarium_data


    def WriteCurrentTerraDataToLog(self):
        ch = ConfigHelper()
        terrarium = ch.GetTerrarium()
        sht21 = SHT21Sensor.objects.all().filter(terrarium=terrarium).first()
        
        if sht21 is None:
            raise Exception('No sensor registered to get terrarium data')
        else:
            time = utils.timezone.now()
            temperature = sht21.read_temperature()
            humidity = sht21.read_humidity()

            terrarium_log = TerrariumLog(time=time,
                                         temperature=temperature,
                                         humidity=humidity,
                                         light=True)
            terrarium_log.save()

    @staticmethod
    def get_terrarium():
        return Terrarium.objects.first()

    @staticmethod
    def get_heater(terrarium):
        return Heater.objects.filter(terrarium=terrarium).first()

    @staticmethod
    def get_light(terrarium):
        return Light.objects.filter(terrarium=terrarium).first()

    @staticmethod
    def get_fogger(terrarium):
        return Fogger.objects.filter(terrarium=terrarium).first()

    @staticmethod
    def get_sprinkler(terrarium):
        return Sprinkler.objects.filter(terrarium=terrarium).first()

    @staticmethod
    def get_fan(terrarium):
        return Fan.objects.filter(terrarium=terrarium).first()

    @staticmethod
    def get_sht21_sensor(terrarium):
        return SHT21Sensor.objects.filter(terrarium=terrarium).first()

    @staticmethod
    def delete_log():
        TerrariumLog.objects.all().delete()

    @staticmethod
    def prevent_caching():
        from django.db import transaction
        transaction.enter_transaction_management()
        transaction.commit()
