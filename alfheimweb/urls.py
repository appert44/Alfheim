# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.contrib.auth.views import login, logout
from django.contrib import admin
from raven.contrib.django.models import client
#from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
import alfheimweb
admin.autodiscover()

from alfheimweb.views import *


urlpatterns = patterns('',                       
                       url(r'^$', Login.as_view(), name='login'),
                       url(r'^main', Main.as_view(), name='main'),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^registration/', 'alfheimweb.views.login'),
                       url(r'^graph/', 'alfheimweb.views.get_graph'),
                       url(r'^sensors/', 'alfheimweb.views.get_sensors'),
                       url(r'^exit/$', 'django.contrib.auth.views.logout',dict(template_name = 'alfheimweb/notlogged.html',),),
                       url(r'^measure', 'alfheimweb.views.measure'),
                       url(r'^h', 'alfheimweb.views.h_agrege'),
                       )
