from django.conf.urls import patterns, url

from terrarium import views

urlpatterns = patterns(
    '',
    url(r'^$', views.index, name='index'),
    url(r'^add_actor/$', views.add_actor, name='add_actor'),
)
