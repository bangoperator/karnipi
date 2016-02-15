from django.core.management.base import NoArgsCommand
from django.conf import settings
import datetime
from camera.models import Picture


class Command(NoArgsCommand):

    def handle_noargs(self, **options):
        now = datetime.datetime.now()
        filename = '{0}-{1}-{2}_{3}{4}.{5}'.format(now.year, now.month, now.day, now.hour, now.minute, 'jpg')
        thumb = 'thumb_{0}-{1}-{2}_{3}{4}.{5}'.format(now.year, now.month, now.day, now.hour, now.minute, 'jpg')
        print filename
        print thumb
        pic = Picture(title = filename,
                      width = 1024,
                      height = 768,
                      source = filename,
                      thumb = thumb,
                      taken_on = now)

        pic.shoot()
        pic.save()
