from __future__ import absolute_import
from django.conf.urls import patterns, url
from config import views 

urlpatterns = patterns(
    '',
    url(r'^$',
        views.index,
        name='index'),
    url(r'^delete_Terrarium',
        views.delete_Terrarium,
        name='delete_Terrarium'),
    url(r'^add_Terrarium.html$',
        views.add_Terrarium,
        name='add_Terrarium'),
    url(r'^add_light.html$',
        views.add_light,
        name='add_light'),
    url(r'^add_heater.html$',
        views.add_heater,
        name='add_heater'),
    url(r'^add_fogger.html$',
        views.add_fogger,
        name='add_fogger'),
    url(r'^add_sprinkler.html$',
        views.add_sprinkler,
        name='add_sprinkler'),
    url(r'^add_fan.html$',
        views.add_fan,
        name='add_fan'),
    url(r'^add_sht21.html$',
        views.add_sht21,
        name='add_sht21'),
    url(r'^add_WeatherURL',
        views.add_WeatherURL,
        name='add_WeatherURL'),
    url(r'^add_Job.html$',
        views.add_Job,
        name='add_Job'),
    url(r'^delete_Job.html$',
        views.delete_job,
        name='delete_job'),
    url(r'^jobs',
        views.jobs,
        name='jobs'),
    url(r'^actors',
        views.actors,
        name='actors'),
    url(r'^sensors',
        views.sensors,
        name='sensors'),
    url(r'^maintenance',
        views.maintenance,
        name='maintenance'),
)
