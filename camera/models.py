import time

from django.conf import settings
from django.db import models

try:
    import picamera
except OSError:
    print "Could not import module 'picamera'. Maybe the module is not enabled in os."

class Picture(models.Model):

    title = models.TextField()
    width = models.CharField(max_length=4, default=640)
    height = models.CharField(max_length=4, default=480)
    source = models.CharField(max_length=100)
    thumb = models.CharField(max_length=100)
    taken_on = models.DateTimeField()

    def shoot(self):

        # sleep for 10 seconds to delay capturing
        time.sleep(10)

        '''
        fswebcam_command = "fswebcam -r {0}x{1} -S 20 --jpeg 100 -s 'Brightness=0%' -s 'Backlight Compensation=30%' --save {2}{3}".format(width, height, settings.MEDIA_ROOT, path)
        os.system(fswebcam_command)

        '''

        # original

        camera = picamera.PiCamera()
        camera.resolution = (self.width, self.height)
        camera. hflip = False
        camera.start_preview()

        # Camera warm-up time
        time.sleep(2)

        camera.capture(settings.MEDIA_ROOT + self.source)

        # thumbnail

        camera.resolution = (320, 240)
        camera. hflip = False
        camera.start_preview()

        # Camera warm-up time
        time.sleep(2)

        camera.capture(settings.MEDIA_ROOT + self.thumb)

