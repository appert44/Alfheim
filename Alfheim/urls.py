# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tuto_django.views.home', name='home'),
    # url(r'^tuto_django/', include('tuto_django.foo.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
