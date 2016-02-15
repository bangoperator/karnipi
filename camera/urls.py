from __future__ import absolute_import
from django.conf.urls import patterns, url
from camera import views

urlpatterns = patterns(
    '',
    url(r'^$',
        views.index,
        name='index'),
)
