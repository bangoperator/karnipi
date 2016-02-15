__author__ = 'bangoperator'

from time import sleep
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):

	import os
	
	mode = int(args[0])

	if mode == 1:
		os.system("sudo service cron stop")
	elif mode == 0:
		os.system("sudo service cron start")
