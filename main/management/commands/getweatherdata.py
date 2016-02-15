from django.core.management.base import NoArgsCommand
from django import utils
from main.models import KarniPiLog
from config.models import Config
from weather.helper import WeatherHelper


class Command(NoArgsCommand):
    def handle_noargs(self, **options):
        wh = WeatherHelper()
        wh.WriteCurrentWeatherDataToLog()
        config = Config.objects.first()
        log = KarniPiLog(
            type='INFO',
            datetime=utils.timezone.now(),
            message='Fetched weather data from {0}'.format(config.weatherURL))
        log.save()
