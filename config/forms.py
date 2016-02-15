from __future__ import absolute_import

from django import forms
from terrarium.models import Terrarium
from . import helper as config_helper

ch = config_helper.ConfigHelper()


class NewLightForm(forms.Form):
    title = forms.CharField(label='Bezeichnung')
    chip_address = forms.CharField(label='Chip-Adresse (0x__)', max_length=2)
    data_address = forms.CharField(label='Daten-Adresse (0x__)', max_length=2)
    value_address = forms.CharField(label='Wert-Adresse (0x__)', max_length=2)
    terrarium = forms.ModelChoiceField(queryset=Terrarium.objects.all())


class NewHeaterForm(forms.Form):
    title = forms.CharField(label='Bezeichnung')
    data_address = forms.CharField(label='Daten-Adresse (0x__)', max_length=2)
    value_address = forms.CharField(label='Wert-Adresse (0x__)', max_length=2)
    chip_address = forms.CharField(label='Chip-Adresse (0x__)', max_length=2)
    data_address = forms.CharField(label='Daten-Adresse (0x__)', max_length=2)
    value_address = forms.CharField(label='Wert-Adresse (0x__)', max_length=2)
    terrarium = forms.ModelChoiceField(queryset=Terrarium.objects.all())


class NewFoggerForm(forms.Form):
    title = forms.CharField(label='Bezeichnung')
    chip_address = forms.CharField(label='Chip-Adresse (0x__)', max_length=2)
    data_address = forms.CharField(label='Daten-Adresse (0x__)', max_length=2)
    value_address = forms.CharField(label='Wert-Adresse (0x__)', max_length=2)
    terrarium = forms.ModelChoiceField(queryset=Terrarium.objects.all())


class NewSprinklerForm(forms.Form):
    title = forms.CharField(label='Bezeichnung')
    chip_address = forms.CharField(label='Chip-Adresse (0x__)', max_length=2)
    data_address = forms.CharField(label='Daten-Adresse (0x__)', max_length=2)
    value_address = forms.CharField(label='Wert-Adresse (0x__)', max_length=2)
    terrarium = forms.ModelChoiceField(queryset=Terrarium.objects.all())


class NewFanForm(forms.Form):
    title = forms.CharField(label='Bezeichnung')
    chip_address = forms.CharField(label='Chip-Adresse (0x__)', max_length=2)
    data_address = forms.CharField(label='Daten-Adresse (0x__)', max_length=2)
    value_address = forms.CharField(label='Wert-Adresse (0x__)', max_length=2)
    terrarium = forms.ModelChoiceField(queryset=Terrarium.objects.all())


class NewSHT21Form(forms.Form):
    title = forms.CharField(label='Bezeichnung')
    bank = forms.CharField(max_length=2)
    address = forms.CharField(max_length=4)
    terrarium = forms.ModelChoiceField(queryset=Terrarium.objects.all())


class NewJobForm(forms.Form):
    title = forms.CharField(label='Titel')
    command = forms.ChoiceField(label='Befehl',
                                choices=ch.GetCustomCommands())
    minute = forms.CharField(label='Minute', min_length=1, max_length=2)
    hour = forms.CharField(label='Stunde', min_length=1, max_length=2)
    day = forms.CharField(label='Tag', min_length=1, max_length=2)
    month = forms.CharField(label='Monat', min_length=1, max_length=2)
    
    # Prevent caching choice values
    def __init__(self, *args, **kwargs):
        super(NewJobForm, self).__init__(*args, **kwargs)
        self.fields['command'] = forms.ChoiceField(choices=ch.GetCustomCommands())

        # self.fields['command'].choices = forms.ChoiceField(ConfigHelper.GetCustomCommands())


class DeleteJobForm(forms.Form):
    title = forms.ChoiceField(choices=ch.GetCronTabsTuples())
    
    # Prevent caching choice values
    def __init__(self, *args, **kwargs):
        super(DeleteJobForm, self).__init__(*args, **kwargs)
        self.fields['title'].choices = ch.GetCronTabsTuples()


class NewTerrariumForm(forms.Form):
    title = forms.CharField()
    temperature_min = forms.CharField(max_length=2)
    temperature_max = forms.CharField(max_length=2)
    sunrise = forms.TimeField()
    sunset = forms.TimeField()
