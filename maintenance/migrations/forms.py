from __future__ import absolute_import

from django import forms
from terrarium.models import Terrarium
from . import helper as config_helper

ch = config_helper.ConfigHelper()


class MaintenanceForm(forms.Form):
    maintenance = forms.BooleanField(default=False)