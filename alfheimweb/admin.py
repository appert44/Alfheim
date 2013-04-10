#-*- coding: utf-8 -*-
from django.contrib import admin
from django.db import models
from raven.contrib.django.models import client

class CaptureAdmin(admin.ModelAdmin):
    list_display = ('id', 'time', 'device', 'sensor_type', 'value', )
    list_filter = ('device', 'sensor_type', )


admin.site.register(models.get_model('alfheimweb', 'Capture'), CaptureAdmin)

class DeviceAdmin(admin.ModelAdmin):
	pass


admin.site.register(models.get_model('alfheimweb', 'Device'), DeviceAdmin)