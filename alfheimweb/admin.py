#-*- coding: utf-8 -*-
from django.contrib import admin
from django.db import models
from raven.contrib.django.models import client

class TableBrutAdmin(admin.ModelAdmin):
    list_display = ('id', 'time', 'device', 'sensor_type', 'value', )
    list_filter = ('device', 'sensor_type', )


admin.site.register(models.get_model('alfheimweb', 'TableBrut'), TableBrutAdmin)

class DeviceAdmin(admin.ModelAdmin):
    list_display = ('serial_number', 'user', )
    list_filter = ('serial_number', )


admin.site.register(models.get_model('alfheimweb', 'Device'), DeviceAdmin)

class H_agregationAdmin(admin.ModelAdmin):
    list_display = ('id', 'time', 'device', 'sensor_type', 'value', )
    list_filter = ('device', 'sensor_type', )


admin.site.register(models.get_model('alfheimweb', 'H_agregation'), H_agregationAdmin)

class D_agregationAdmin(admin.ModelAdmin):
    list_display = ('id', 'time', 'device', 'sensor_type', 'value', )
    list_filter = ('device', 'sensor_type', )


admin.site.register(models.get_model('alfheimweb', 'D_agregation'), D_agregationAdmin)

class M_agregationAdmin(admin.ModelAdmin):
    list_display = ('id', 'time', 'device', 'sensor_type', 'value', )
    list_filter = ('device', 'sensor_type', )


admin.site.register(models.get_model('alfheimweb', 'M_agregation'), M_agregationAdmin)

class Y_agregationAdmin(admin.ModelAdmin):
    list_display = ('id', 'time', 'device', 'sensor_type', 'value', )
    list_filter = ('device', 'sensor_type', )


admin.site.register(models.get_model('alfheimweb', 'Y_agregation'), Y_agregationAdmin)



