import sys
from django.conf import settings
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.views.decorators.cache import never_cache
from config.helper import ConfigHelper
from main.helper import MainHelper
from terrarium.helper import TerrariumHelper


@never_cache
def index(request):

    status_overview = MainHelper().get_status_overview()
    config = ConfigHelper().GetConfig()

    file_object = open(settings.BASE_DIR + '/main/logging/karnipi.log', 'r')
    log = file_object.read()
    file_object.close()

    if request.method == "POST":
        mode = request.POST.get('maintenance_mode', '')

        if mode == "an":
            config.maintenance = True
        else:
            config.maintenance = False

        config.save()

        template = loader.get_template('maintenance/index.html')
        context = RequestContext(request, {
        'status_overview': status_overview,
        'current_site': 'maintenance',
        'log': log,
        'maintenance_mode': config.maintenance,
        })
        print context
        return HttpResponse(template.render(context))

    else:
        print "doing something"
        template = loader.get_template('maintenance/index.html')
        context = RequestContext(request, {
            'status_overview': status_overview,
            'current_site': 'maintenance',
            'log': log,
            'maintenance_mode': config.maintenance,
        })
        return HttpResponse(template.render(context))
