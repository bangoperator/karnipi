
from django.conf.urls import patterns, include, url, handler500
handler500 = 'karnipi.main.views.server_error'

from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from main import views as mainviews


admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', include('main.urls', namespace="main")),
    url(r'^main/', include('main.urls', namespace="main")),
    url(r'^maintenance/', include('maintenance.urls', namespace="maintenance")),
    url(r'^config/', include('config.urls', namespace="config")),
    url(r'^camera/', include('camera.urls', namespace="camera")),
    url(r'^weather/', include('weather.urls', namespace="weather")),
    url(r'^terrarium/', include('terrarium.urls', namespace="terrarium")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
