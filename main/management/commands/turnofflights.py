from django.core.management.base import NoArgsCommand

from terrarium.models import Light
from config.models import Config

import sys
sys.path.insert(1, '/usr/lib/python2.7/dist-packages/')

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'karnipi.settings')



class Command(NoArgsCommand):
    def handle_noargs(self, **options):
        
        config = Config.objects.first()
        terrarium = config.terrarium

        light = Light.objects.filter(terrarium=terrarium).first()
        
        if light is not None:
            light.off()

        terrarium.sleep()