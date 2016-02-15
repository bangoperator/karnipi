from __future__ import absolute_import

from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django import utils

from config.helper import ConfigHelper
from config.models import Config
from config.forms import NewLightForm, NewHeaterForm, NewFoggerForm, NewSprinklerForm, NewFanForm, NewJobForm, DeleteJobForm, \
    NewTerrariumForm, NewSHT21Form
from terrarium.models import Terrarium, Light, Heater, Fogger, Sprinkler, Fan, I2CActor, I2CSensor, SHT21Sensor as SHT21
from main.models import KarniPiLog
from main.logger import KarniLogger
from main.helper import MainHelper


def index(request):
    ch = ConfigHelper()
    crons = ch.GetCronTabs()
    config = ch.GetConfig()

    if config is None:
        config = ch.CreateConfig()

    light = None
    heater = None
    fogger = None
    fan = None
    sht21 = None
    status_overview = None
    maintenance = None
    disk_space = None

    disk_space = ch.disk_usage()
    usage = int(disk_space[0])
    free = int(disk_space[1])

    if config.maintenance:
            status_overview = MainHelper().get_status_overview()

    terrarium = config.terrarium

    if terrarium is not None:
        light = Light.objects.filter(terrarium=terrarium)
        heater = Heater.objects.filter(terrarium=terrarium)
        fogger = Fogger.objects.filter(terrarium=terrarium)
        sprinkler = Sprinkler.objects.filter(terrarium=terrarium)
        fan = Fan.objects.filter(terrarium=terrarium)
        sht21 = SHT21.objects.filter(terrarium=terrarium)

    template = loader.get_template('config/index.html')
    context = RequestContext(request, {
        'crons': crons,
        'config': config,
        'terrarium': terrarium,
        'light': light,
        'heater': heater,
        'fogger': fogger,
        'sprinkler': sprinkler,
        'fan': fan,
        'sht21': sht21,
        'status_overview': status_overview,
        'maintenance': config.maintenance,
        'disk_space_usage': usage,
	'disk_space_free': free,
        'current_site': 'config',
    })
    return HttpResponse(template.render(context))


def jobs(request):
    ch = ConfigHelper()
    crons = ch.GetCronTabs()
    template = loader.get_template('config/jobs.html')
    context = RequestContext(request, {
        'crons': crons,
    })
    return HttpResponse(template.render(context))


def actors(request):
    config = ConfigHelper().GetConfig()
    objects = config.terrarium.get_actors()
    template = loader.get_template('config/actors.html')
    context = RequestContext(request, {
        'actors': objects,
    })
    return HttpResponse(template.render(context))


def sensors(request):
    config = ConfigHelper().GetConfig()
    objects = config.terrarium.get_sensors()
    template = loader.get_template('config/sensors.html')
    context = RequestContext(request, {
        'sensors': objects,
    })
    return HttpResponse(template.render(context))


def maintenance(request):
    config = ConfigHelper().GetConfig()
    status_overview = None

    if config.maintenance:
            status_overview = MainHelper().get_status_overview()

    template = loader.get_template('config/maintenance.html')
    context = RequestContext(request, {
        'status_overview': status_overview,
    })
    return HttpResponse(template.render(context))

def delete_Terrarium(request):
    config = Config.objects.all().first()
    terrarium = config.terrarium

    config.terrarium = None
    config.save()

    heater = Heater.objects.filter(terrarium_id=terrarium.id)
    fogger = Fogger.objects.filter(terrarium_id=terrarium.id)
    heater.all().delete()
    fogger.all().delete()

    title = terrarium.title

    try:
        Terrarium.objects.get(id=terrarium.id).delete()
        log = KarniPiLog(type='INFO',
                         datetime=utils.timezone.now(),
                         message="Terrarium '{0}' wurde aus der Konfiguration "
                                 + "entfernt".format(title))
        log.save()
    except:
        log = KarniPiLog(type='INFO',
                         datetime=utils.timezone.now(),
                         message="Es ist ein Fehler beim Entfernen des "
                                 + "Terrarium '{0}' aufgetreten".format(title))
        log.save()

    config = ConfigHelper().GetConfig()

    url = reverse('config:index')
    return HttpResponseRedirect(url)


def delete_job(request):
    if request.method == 'GET':
        form = DeleteJobForm()
    else:
        form = DeleteJobForm(request.POST)

        url = None

        if form.is_valid():
            str_title = None
            job_title_id = form.cleaned_data['title']
            choices = form.fields['title'].choices

            for c in choices:
                if int(job_title_id) == int(c[0]):
                    str_title = str(c[1])
                    break

            ConfigHelper().DeleteCronJob(str_title)

            url = reverse('config:index')

        return HttpResponseRedirect(url)
    return render(request, 'config/delete_Job.html', {'form': form})


def add_sht21(request):
    if request.method == 'GET':
        form = NewSHT21Form()
    else:
        form = NewSHT21Form(request.POST)

        if form.is_valid():
            sht_title = form.cleaned_data['title']
            sht_bank = form.cleaned_data['bank']
            sht_address = form.cleaned_data['address']
            sht_terra = form.cleaned_data['terrarium']
            SHT21.objects.create(title=sht_title,
                                 bank=sht_bank,
                                 address=sht_address,
                                 terrarium=sht_terra)

            url = reverse('config:index')

        return HttpResponseRedirect(url)
    return render(request, 'config/add_sht21.html', {'form': form})


def add_heater(request):
    if request.method == 'GET':
        form = NewHeaterForm()
    else:
        form = NewHeaterForm(request.POST)

        url = None

        if form.is_valid():
            title = form.cleaned_data['title']
            chip_address = form.cleaned_data['chip_address']
            data_address = form.cleaned_data['data_address']
            value_address = form.cleaned_data['value_address']
            terrarium = form.cleaned_data['terrarium']
            Heater.objects.create(title=title,
                                  chip_address=chip_address,
                                  data_address=data_address,
                                  value_address=value_address,
                                  terrarium=terrarium)

            url = reverse('config:index')

        return HttpResponseRedirect(url)
    return render(request, 'config/add_heater.html', {'form': form})


def add_light(request):
    if request.method == 'GET':
        form = NewLightForm()
    else:
        form = NewLightForm(request.POST)

        url = None

        if form.is_valid():
            title = form.cleaned_data['title']
            chip_address = form.cleaned_data['chip_address']
            data_address = form.cleaned_data['data_address']
            value_address = form.cleaned_data['value_address']
            terrarium = form.cleaned_data['terrarium']
            Light.objects.create(title=title,
                                 chip_address=chip_address,
                                 data_address=data_address,
                                 value_address=value_address,
                                 terrarium=terrarium)

            url = reverse('config:index')

        return HttpResponseRedirect(url)
    return render(request, 'config/add_light.html', {'form': form})


def add_fogger(request):
    if request.method == 'GET':
        form = NewFoggerForm()
    else:
        form = NewFoggerForm(request.POST)

        if form.is_valid():
            title = form.cleaned_data['title']
            chip_address = form.cleaned_data['chip_address']
            data_address = form.cleaned_data['data_address']
            value_address = form.cleaned_data['value_address']
            terrarium = form.cleaned_data['terrarium']

            Fogger.objects.create(title=title,
                                  chip_address=chip_address,
                                  data_address=data_address,
                                  value_address=value_address,
                                  terrarium=terrarium)

            url = reverse('config:index')

        return HttpResponseRedirect(url)
    return render(request, 'config/add_fogger.html', {'form': form})


def add_sprinkler(request):
    if request.method == 'GET':
        form = NewSprinklerForm()
    else:
        form = NewSprinklerForm(request.POST)

        if form.is_valid():
            title = form.cleaned_data['title']
            chip_address = form.cleaned_data['chip_address']
            data_address = form.cleaned_data['data_address']
            value_address = form.cleaned_data['value_address']
            terrarium = form.cleaned_data['terrarium']

            Sprinkler.objects.create(title=title,
                                  chip_address=chip_address,
                                  data_address=data_address,
                                  value_address=value_address,
                                  terrarium=terrarium)

            url = reverse('config:index')

        return HttpResponseRedirect(url)
    return render(request, 'config/add_sprinkler.html', {'form': form})


def add_fan(request):
    if request.method == 'GET':
        form = NewFanForm()
    else:
        form = NewFanForm(request.POST)

        if form.is_valid():
            title = form.cleaned_data['title']
            chip_address = form.cleaned_data['chip_address']
            data_address = form.cleaned_data['data_address']
            value_address = form.cleaned_data['value_address']
            terrarium = form.cleaned_data['terrarium']

            Fan.objects.create(title=title,
                               chip_address=chip_address,
                               data_address=data_address,
                               value_address=value_address,
                               terrarium=terrarium)

            url = reverse('config:index')

        return HttpResponseRedirect(url)
    return render(request, 'config/add_fan.html', {'form': form})


def add_Job(request):

    if request.method == 'GET':
        form = NewJobForm()
    else:
        form = NewJobForm(request.POST)

        from karnipi import settings

        settings.BASE_DIR

        python_path = "{0}/bin/python".format(settings.BASE_DIR)
        django_manage_path = "{0}/manage.py".format(settings.BASE_DIR)

        if form.is_valid():
            job_title = form.cleaned_data['title']
            int_command = form.cleaned_data['command']

            choices = dict(form.fields['command'].choices)
            for c in choices:
                if int(c) == int(int_command):
                    str_command = str(choices[c])
                    break

            job_command = "{0} {1} {2}".format(python_path,
                                               django_manage_path,
                                               str_command)

            KarniLogger().log_debug("Adding job as crontab entry " + str(job_command))

            job_minute = form.cleaned_data['minute']
            job_hour = form.cleaned_data['hour']
            job_day = form.cleaned_data['day']
            job_month = form.cleaned_data['month']

            ConfigHelper().CreateCronJob(job_command,
                                 job_title,
                                 job_hour,
                                 job_minute,
                                 job_day, job_month)

            url = reverse('config:index')
            return HttpResponseRedirect(url)

    return render(request, 'config/add_Job.html', {'form': form})


def add_WeatherURL(request):
    weatherURL = request.POST.get('inputWeatherURL')
    ch = ConfigHelper()
    config = ch.GetConfig()
    config.weatherURL = weatherURL
    config.save()

    url = reverse('config:index')
    return HttpResponseRedirect(url)


def add_Terrarium(request):
    if request.method == 'GET':
        form = NewTerrariumForm()
    else:
        form = NewTerrariumForm(request.POST)

        config = ConfigHelper().GetConfig()

        if form.is_valid():
            terra_title = form.cleaned_data['title']
            terra_temperature_min = form.cleaned_data['temperature_min']
            terra_temperature_max = form.cleaned_data['temperature_max']
            terra_sunrise = form.cleaned_data['sunrise']
            terra_sunset = form.cleaned_data['sunset']

            if config is None:
                raise Exception('Configuration not found...')
            else:
                terrarium = Terrarium.objects.create(title=terra_title,
                                                     temperature_min=terra_temperature_min,
                                                     temperature_max=terra_temperature_max,
                                                     sunrise=terra_sunrise,
                                                     sunset=terra_sunset)

                if config.terrarium is None:
                    config.terrarium = terrarium
                    config.save()

                    url = reverse('config:index')
                    return HttpResponseRedirect(url)
                else:
                    terrarium.delete()
                    raise Exception('There is already a terrarium configured...')

    return render(request, 'config/add_Terrarium.html', {'form': form})


