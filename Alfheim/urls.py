#-*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

from Alfheimweb.views import TasksView

urlpatterns = patterns('',
    # Examples:
	url(r'^$', TasksView.as_view(), name='Alfheimweb'), 
	url(r'^measure', 'Alfheimweb.views.measure'),
 # url(r'^tuto_django/', include('tuto_django.foo.urls')),

	url(r'^admin/', include(admin.site.urls)),
)
