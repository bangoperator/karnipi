from django.db import models
from terrarium.models import Terrarium


class Config(models.Model):
    weatherURL = models.TextField()
    terrarium = models.ForeignKey(Terrarium, null=True)
    maintenance = models.BooleanField(default=False)