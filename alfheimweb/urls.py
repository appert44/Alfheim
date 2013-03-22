# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.contrib.auth.views import login, logout
from django.contrib import admin
import alfheimweb
admin.autodiscover()

from alfheimweb.views import *


urlpatterns = patterns('',
                       url(r'^$', Login.as_view(), name='login'),
                       url(r'^main', Main.as_view(), name='main'),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^registration/', 'alfheimweb.views.login'),
                       url(r'^measure', 'alfheimweb.views.measure'),
                       )
