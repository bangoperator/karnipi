from __future__ import absolute_import
from datetime import datetime
from django.views.decorators.cache import never_cache
from django.http import HttpResponse
from django.template import RequestContext, loader

from .models import TerrariumLog
from .helper import TerrariumHelper

@never_cache
def index(request):

    today = datetime.today()
    latest_terrarium_log = TerrariumLog.objects.all().filter(time__year=today.year,
                                                             time__month=today.month,
                                                             time__day=today.day).order_by('-time')

    template = loader.get_template('terrarium/index.html')
    context = RequestContext(request, {
        'latest_terrarium_log': latest_terrarium_log,
        'current_site': 'terrarium_data',
    })
    return HttpResponse(template.render(context))
