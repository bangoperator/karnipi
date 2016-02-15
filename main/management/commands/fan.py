__author__ = 'bangoperator'

from time import sleep
from django.core.management.base import NoArgsCommand
from terrarium.helper import TerrariumHelper


class Command(NoArgsCommand):
    def handle_noargs(self, **options):

        th = TerrariumHelper()
        terrarium = th.get_terrarium()

        if terrarium is not None:

            if terrarium.is_sleeping() is False:

                fan = th.get_fan(terrarium)

                if fan is not None:
                    fan.on()
                    sleep(5*60)
                    fan.off()
