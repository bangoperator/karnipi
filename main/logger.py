__author__ = 'bangoperator'

from django import utils
import logging


class KarniLogger():

    def __init__(self):
        logging.basicConfig(filename='/home/pi/karnipi/main/logging/karnipi.log', level=logging.INFO)

    @staticmethod
    def log_debug(msg):
        logging.debug('{0} | {1}'.format(utils.timezone.now(), msg))

    @staticmethod
    def log_info(msg):
        logging.info('{0} | {1}'.format(utils.timezone.now(), msg))

    @staticmethod
    def log_warning(msg):
        logging.warning('{0} | {1}'.format(utils.timezone.now(), msg))