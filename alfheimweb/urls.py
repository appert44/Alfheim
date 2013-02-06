# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

from alfheimweb.views import *


urlpatterns = patterns('',
                       url(r'^$', Login.as_view(), name='login'),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^measure', 'alfheimweb.views.measure'),
                       )
