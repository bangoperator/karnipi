from main.models import KarniPiLog
from terrarium.models import I2CActor
from terrarium.helper import TerrariumHelper


class MainHelper():

    @staticmethod
    def get_karnipi_log():
        # doing .objects instead of objects.all()
        # gives the possibility to sort results
        return KarniPiLog.objects.all()

    @staticmethod
    def get_status_overview():

        th = TerrariumHelper()
        terrarium = th.get_terrarium()
        heater = th.get_heater(terrarium)
        light = th.get_light(terrarium)
        fogger = th.get_fogger(terrarium)
        sprinkler = th.get_sprinkler(terrarium)
        fan = th.get_fan(terrarium)

        status = []

        for i in I2CActor.objects.all():
            status.append(i)

        return status
