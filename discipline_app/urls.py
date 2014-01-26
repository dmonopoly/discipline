from django.conf.urls import patterns, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('discipline_app.views',
  url(r'^$', 'index', name='index'),
  url(r'^signup/$', 'signup', name='signup')
)
# urlpatterns += staticfiles_urlpatterns()
