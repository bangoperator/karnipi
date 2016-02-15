from __future__ import absolute_import
from django.test import TestCase
from .models import Config


class ConfigTestCase(TestCase):
    def setUp(self):
        Config.objects.create(weatherURL='http://api.wunderground.com/api/'
                              + 'a54a0edf42848e04/geolookup/conditions/'
                              + 'astronomy/q/1.058064,114.232401.json')

    def test_get_weather_data(self):
        """Config object that return a json
        weather string is correctly created"""
        config = Config.objects.first()
        return 'The json data which comes from the weather station is: {0}'.format(config.weatherURL)
