from django.core.management.base import NoArgsCommand
from django import utils
from main.models import KarniPiLog
from terrarium.helper import TerrariumHelper
from karnipi import sht21


class Command(NoArgsCommand):
    def handle_noargs(self, **options):
        
        th = TerrariumHelper()
        th.WriteCurrentTerraDataToLog()
