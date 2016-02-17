__author__ = 'bangoperator'

from django import utils
from django.conf import settings
import logging


class KarniLogger():

    def __init__(self):
        logpath = settings.BASE_DIR + '/main/logging/karnipi.log'
        logging.basicConfig(filename=logpath, level=logging.INFO)

    @staticmethod
    def log_debug(msg):
        logging.debug('{0} | {1}'.format(utils.timezone.now(), msg))

    @staticmethod
    def log_info(msg):
        logging.info('{0} | {1}'.format(utils.timezone.now(), msg))

    @staticmethod
    def log_warning(msg):
        logging.warning('{0} | {1}'.format(utils.timezone.now(), msg))