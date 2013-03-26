# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.contrib.auth.views import login, logout
from django.contrib import admin
from raven.contrib.django.models import client
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
import alfheimweb
admin.autodiscover()

from alfheimweb.views import *


urlpatterns = patterns('',
                       #(r'^$', login_required(TemplateView.as_view(template_name='login.html'))),
                       
                       url(r'^$', Login.as_view(), name='login'),
                       url(r'^main', Main.as_view(), name='main'),
                       #url(r'^test', Test.as_view(), name='test'),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^registration/', 'alfheimweb.views.login'),
                       #url(r'^exit/', 'alfheimweb.views.login'),
                       url(r'^exit/$', 'django.contrib.auth.views.logout',dict(template_name = 'alfheimweb/notlogged.html',),),
                       url(r'^measure', 'alfheimweb.views.measure'),
                       )
