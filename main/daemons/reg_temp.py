#!/usr/bin/env python

import logging
import time
import datetime


class TemperatureRegulator():

    start_time = None
    end_time = None
    end_time_cycle = None
    counter = 0

    def __init__(self):
        self.start_time = time.time()
        self.end_time = self.start_time+1*60
        self.end_time_cycle = self.start_time+2*60

        logging.basicConfig(
            filename='/var/log/karnipi_temp_reg.log',
            level=logging.DEBUG,
            format='%(asctime)s [%(levelname)s] %(message)s')

        logging.info('initialized temperature regulator...')

    def run(self):
        logging.info('regulating temperature')
        
        formatted_start_time = datetime.datetime.fromtimestamp(self.start_time).strftime('%Y-%m-%d %H:%M:%S')
        formatted_end_time = datetime.datetime.fromtimestamp(self.end_time).strftime('%Y-%m-%d %H:%M:%S')
        
        logging.info('start time: {0}'.format(formatted_start_time))
        logging.info('end time: {0}'.format(formatted_end_time))

        while time.time() <= self.end_time_cycle:
            time.sleep(10)
            while time.time() <= self.end_time:
                    logging.info('regulating...time: {0}'.format(time.time()))
                    time.sleep(30)

            time.sleep(30)
            logging.info('temp cycle idling')
        logging.info('temp cycle done')

tr = TemperatureRegulator()
tr.run()
