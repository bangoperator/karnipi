import sys
sys.path.insert(1, '/usr/lib/python2.7/dist-packages/')
import smbus
from time import sleep

from django.core.management.base import BaseCommand
from django import utils

from main.models import KarniPiLog
from terrarium.models import Sprinkler
from config.models import Config



class Command(BaseCommand):
    args = '<time time ...>'

    def handle(self, *args, **options):

        config = Config.objects.first()
        terrarium = config.terrarium
        duration = None

        if terrarium.is_sleeping() is False:
            for time in args:
                duration = int(time)

            IODIRA = 0x00 # Pin direction register



            # get fogger address data

            sprinkler = Sprinkler.objects.filter(terrarium=terrarium).first()

            if sprinkler is not None:
                sprinkler.on()
                sleep(15)
                sprinkler.off()