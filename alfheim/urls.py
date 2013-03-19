# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.views.generic import RedirectView

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^$', RedirectView.as_view(url='alfheimweb/')),
                       url(r'^alfheimweb/', include('alfheimweb.urls')),
                       )
    # Examples:
    # url(r'^$', 'alfheim.views.home', name='home'),
    # url(r'^alfheim/', include('alfheim.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
