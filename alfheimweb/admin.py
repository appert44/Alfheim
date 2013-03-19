#-*- coding: utf-8 -*-
from django.contrib import admin
from django.db import models


class CaptureAdmin(admin.ModelAdmin):
    list_display = ('id', 'time', 'device_sn', 'sensor_type', 'value', )
    list_filter = ('device_sn', 'sensor_type', )

admin.site.register(models.get_model('alfheimweb', 'Capture'), CaptureAdmin)
