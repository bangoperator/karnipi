import os
import sys

from django.core.wsgi import get_wsgi_application

sys.path.append('/home/pi/karnipi/')

os.environ['DJANGO_SETTINGS_MODULE'] = 'karnipi.settings'
application = get_wsgi_application()

#activate_this='/home/pi/karnipi/bin/activate_this.py'
#execfile(activate_this, dict(__file__=activate_this))
