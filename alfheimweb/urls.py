# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.contrib.auth.views import login, logout
from django.contrib import admin
from raven.contrib.django.models import client
import alfheimweb
admin.autodiscover()

from alfheimweb.views import *


urlpatterns = patterns('',
                       url(r'^$', Login.as_view(), name='login'),
                       url(r'^main', Main.as_view(), name='main'),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^test/', 'alfheimweb.views.login'),
                       url(r'^measure', 'alfheimweb.views.measure'),
                       url(r'^accounts/login/$',  login),
                       url(r'^accounts/logout/$', logout),
                       )
