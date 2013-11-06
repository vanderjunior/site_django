# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^polls/$', 'mysite.polls.views.index'),
    url(r'^polls/(?P<poll_id>\d+)/$', 'mysite.polls.views.detail'),
    url(r'^polls/(?P<poll_id>\d+)/results/$', 'mysite.polls.views.results'),
    url(r'^polls/(?P<poll_id>\d+)/vote/$', 'mysite.polls.views.vote'),
    # (r'^admin/(.*)', admin.site.root),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
