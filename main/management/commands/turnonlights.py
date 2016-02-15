from django.core.management.base import NoArgsCommand

from terrarium.models import Light
from config.models import Config


class Command(NoArgsCommand):
    def handle_noargs(self, **options):
        
        config = Config.objects.first()
        terrarium = config.terrarium

        terrarium.wake_up()

        light = Light.objects.filter(terrarium=terrarium).first()

        if light is not None:
            light.on()


