import logging
import sys
import daemonocle

import threading
from subprocess import Popen, PIPE
import multiprocessing
import time


from django import utils

# insert karnipi root path into environment var
sys.path.insert(1, '/home/pi/karnipi/')

# set project settings module
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'karnipi.settings')

from terrarium.helper import TerrariumHelper

import django
django.setup()

from main.logger import KarniLogger

"""
class Control(threading.Thread):

    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        print "Starting " + self.name

        # preparing the shell command to call the django custom command
        shell_command = 'python /home/pi/karnipi/manage.py {0} {1}'.format(self.name,
                                                                           self.counter)

        # open subprocess to exec the shell command
        p = Popen(
            shell_command.split(),
            shell=False,
            stdout=PIPE,
            stderr=PIPE)
"""


class KarniPiControl():

    action = None

    def __init__(self):
        KarniLogger().log_info("Init control...")

    @staticmethod
    def get_exit_code():
        file_object = open('/home/pi/karnipi/main/daemons/exit.txt', 'r')
        sys_exit = file_object.read()
        file_object.close()
        return sys_exit

    def handle_control(self, terrarium):

        if self.action is None:
            self.action = "heating"

        KarniLogger().log_info("Getting terrarium data...")
        sht21 = TerrariumHelper().get_sht21_sensor(terrarium)
        print sht21
        temperature = int(sht21.read_temperature())
        print temperature
        # terra_data = TerrariumHelper().GetCurrentTerrariumData()

        KarniLogger().log_info("Accessing heater...")
        heater = TerrariumHelper().get_heater(terrarium)

        # if heater is available
        if heater is not None:
            KarniLogger().log_info("Terrarium: {0} C".format(int(temperature)))
            KarniLogger().log_info("Ziel-Temperatur: {0} C".format(int(terrarium.temperature_max)))
            KarniLogger().log_info("Action is '{0}'".format(self.action))

            if int(temperature) < int(terrarium.temperature_min):
                self.action = "heating"
                heater.on()
                KarniLogger().log_info("Heating...")
            elif (int(temperature) <= int(terrarium.temperature_max)) & (self.action == "heating"):
                heater.on()
            elif (int(temperature) <= int(terrarium.temperature_max)) & (self.action == "cool down"):
                heater.off()
            elif int(temperature) > int(terrarium.temperature_max):
                self.action = "cool down"
                heater.off()
                KarniLogger().log_info("Cooling down...")
            else:
                KarniLogger().log_info("Don't know what to do...")


def main():

    control = KarniPiControl()

    # run as far as you can
    while True:
        exit_code = control.get_exit_code()
        KarniLogger().log_info("Checking for exit code..." + str(exit_code))

        if int(exit_code) == 0:
            KarniLogger().log_info("Staring next cycle...")

            try:
                try:
                    terrarium = TerrariumHelper().get_terrarium()
                except:
                    KarniLogger().log_info("Couldn't get terrarium...")

                if terrarium.sleep_mode is False:
                    control.handle_control(terrarium)
                else:
                    KarniLogger().log_info("Sleeping so well...")

            except (KeyboardInterrupt, SystemExit):
                KarniLogger().log_info("Exiting...")
                sys.exit()
            finally:
                KarniLogger().log_info("Idling for 10 minutes")
                time.sleep(10*60)
        else:
            KarniLogger().log_info("Exiting due to exit code...")
            sys.exit()


if __name__ == "__main__":
    main()


"""
    light = Control(1, "heater", 2)
    fogger = Control(1, "fogger", 1)
    threads = []
    threads.append(light)
    threads.append(fogger)

    # Start all threads
    [x.start() for x in threads]

    # Wait for all of them to finish
    [x.join() for x in threads]
    """