from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
  url(r'^$', include('discipline_app.urls')),
#   url(r'^discipline_app/', include('discipline_app.urls',
#     namespace="discipline_app")),
  url(r'^admin/', include(admin.site.urls)),
)
urlpatterns += staticfiles_urlpatterns()