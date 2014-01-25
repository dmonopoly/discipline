from django.conf.urls import patterns, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from discipline_app import views

urlpatterns = patterns('',
  url(r'^$', views.index, name='index'),
)
urlpatterns += staticfiles_urlpatterns()
