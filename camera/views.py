from __future__ import absolute_import
from datetime import datetime
from django.template import RequestContext, loader
from django.http import HttpResponse, HttpResponseServerError
from django.views.decorators.cache import never_cache

from camera.models import Picture

@never_cache
def index(request):
    try:
        today = datetime.today()
        pictures_today = Picture.objects.all().filter(taken_on__year=today.year,
                                                      taken_on__month=today.month,
                                                      taken_on__day=today.day).order_by('-taken_on')

        if pictures_today is None:
            latest_picture = None
        else:
            latest_picture = pictures_today.latest('taken_on')

        template = loader.get_template('camera/index.html')
        context = RequestContext(request, {
            'latest_picture': latest_picture,
            'pictures_today': pictures_today,
            'current_site': 'camera',
        })
        return HttpResponse(template.render(context))
    except:
        return HttpResponseServerError('Error loading camera page. Maybe no picture has been taken yet...Try again later!')
