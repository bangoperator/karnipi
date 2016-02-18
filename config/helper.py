from config.models import Config
from django.conf import settings
from crontab import CronTab
import os
import getpass


class ConfigHelper:
    
    user = getpass.getuser()

    def GetCronTabs(self):    
        tab = CronTab(user=self.user)
        return tab.crons
    
    
    def GetCronTabsTuples(self):
        crons = self.GetCronTabs()
    
        ret_list = []
        index = 0
    
        for c in crons:
            ret_list.append((index, c.comment))
            index = index + 1
        return ret_list
    
    
    def GetConfig(self):

        if Config.objects.count() == 0:
            Config.objects.create()

        config = Config.objects.all().first()
        return config
    
    
    def CreateConfig(self):
        return Config.objects.create(maintenance=False)
    
    
    def GetTerrarium(self):
        config = Config.objects.all().first()
        terrarium = config.terrarium
    
        return terrarium
    
    
    def GetCustomCommands(self):
        from django.core.management import get_commands
        
        idx = 0
        commands = [(idx, '-- bitte waehlen --')]
        for command_name, app_name in get_commands().items():
            if app_name == 'main':
                idx=idx+1
                commands.append((idx, command_name))
    
        return commands
    
    
    def CreateCronJob(self, cmd, description, hour, minute, day, month):
        tab = CronTab(user=self.user)
        cmd = cmd
    
        # You can even set a comment for this command
        cron_job = tab.new(cmd, comment=description)
    
        if hour is not None and hour != "*":
            cron_job.hour.on(hour)
    
        if minute is not None and minute != "*":
            cron_job.minute.on(minute)
    
        if day is not None and day != "*":
            cron_job.day.on(day)
    
        if month is not None and month != "*":
            cron_job.month.on(month)
    
        # writes content to crontab
        tab.write()
        print(tab.render())
    
    
    def DeleteCronJob(self, description):
        tab = CronTab(user=self.user)
    
        for item in tab.find_comment(description):
            tab.remove(item)
    
        # writes content to crontab
        tab.write()


    def get_disk_space(self):
        stat = os.statvfs('/')
        size_mb = (stat.f_bsize * stat.f_bavail / 1024 / 1024)
	return size_mb

    def disk_usage(self):
	st = os.statvfs('/')
	free = st.f_bavail * st.f_frsize / 1024 / 1024
	total = st.f_blocks * st.f_frsize / 1024 / 1024
	used = ((st.f_blocks - st.f_bfree) * st.f_frsize) / 1024 / 1024
	
	return [used, free]
