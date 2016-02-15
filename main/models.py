from django.db import models


class KarniPiLog(models.Model):
    type = models.TextField()
    datetime = models.DateTimeField()
    message = models.TextField()
