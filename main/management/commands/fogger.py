import sys
sys.path.insert(1, '/usr/lib/python2.7/dist-packages/')
import smbus
from time import sleep

from django.core.management.base import NoArgsCommand
from terrarium.models import Fogger
from terrarium.helper import TerrariumHelper
from config.models import Config


class Command(NoArgsCommand):
    def handle_noargs(self, **options):

        config = Config.objects.first()
        terrarium = config.terrarium
        th = TerrariumHelper()

        if terrarium is not None:
            if terrarium.is_sleeping() is False:

                fogger = th.get_fogger(terrarium)

                if fogger is not None:
                    fogger.on()
                    sleep(20)
                    #sleep(3*60)
                    fogger.off()