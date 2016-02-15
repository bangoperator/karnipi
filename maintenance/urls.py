from django.conf.urls import patterns, url

from maintenance import views

urlpatterns = patterns(
    '',
    url(r'^$', views.index, name='index'),
)
