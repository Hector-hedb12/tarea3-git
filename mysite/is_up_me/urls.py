from django.conf.urls import patterns, url

from is_up_me import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<url_solicitada>[a-z]+)/$', views.consultar, name='consultar'),
)
