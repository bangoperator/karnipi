import logging
import time

from config.helper import ConfigHelper
from terrarium.models import Fogger, Heater, Light

class HumidityRegulator():
    start_time = None
    end_time = None
    end_time_cycle = None
    counter = 0

    def __init__(self):
        self.start_time = time.time()
        self.end_time = self.start_time+1*60
        self.end_time_cycle = self.start_time+2*60

        logging.basicConfig(
            filename='/var/log/daemonocle_example.log',
            level=logging.DEBUG,
            format='%(asctime)s [%(levelname)s] %(message)s')

        logging.info('initialized humidity regulator...')

    def run(self):
        print('Initializing config helper class')
	ch = ConfigHelper()

	config = None
	print('getting config')
	config = ch.GetConfig()

	while config is None:
	    time.sleep(1)
	    print('sleeping...no config')
        
        print(config)
        
        logging.info('regulating humidity')
        logging.info('start time: {0}'.format(self.start_time))
        logging.info('end time: {0}'.format(self.end_time))
        
        time.sleep(10)
        """
        while time.time() <= self.end_time_cycle:
            time.sleep(10)
            while time.time() <= self.end_time:
                    logging.info('regulating...time: {0}'.format(time.time()))
                    time.sleep(30)

            time.sleep(30)
            logging.info('humidity cycle idling')
        logging.info('humidity cycle done')
        """
