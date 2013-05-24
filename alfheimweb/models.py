from django.db import models
from django.conf import settings
from django import forms
from django.forms import ModelForm, PasswordInput
from raven.contrib.django.models import client
from django.utils.dateformat import format
from django.contrib.auth.models import User
import datetime
import time


class Device(models.Model):
    serial_number = models.CharField(max_length=45, primary_key=True)
    user = models.ForeignKey('auth.User', blank=True, null=True, default=None)
    
    def display(self):
        return self.serial_number
    
    def __unicode__(self):
        return u"Device %s" % self.serial_number
    
class TableBrut(models.Model):
    SENSOR_TYPES = (
        ('temp', 'Temperature'),
        ('presence', 'Presence'),
    )
    time = models.DateTimeField()
    sensor_type = models.CharField(max_length=8, choices=SENSOR_TYPES)
    
    value = models.FloatField(blank=True, default=None, null=True)
    device = models.ForeignKey(Device)

    def display(self):
        # capture_time = format(self.time, u'U')
        capture_time = (time.mktime(self.time.timetuple())*1000)
        return int(capture_time) , self.value
    
    def val(self):
        return self.value
    def tps(self):
        return self.time
    
    class Meta:
        ordering = ['-time', ]
class H_agregation(models.Model):
    SENSOR_TYPES = (
        ('temp', 'Temperature'),
        ('presence', 'Presence'),
    )
    time = models.DateTimeField()
    sensor_type = models.CharField(max_length=8, choices=SENSOR_TYPES)
    
    value = models.FloatField(blank=True, default=None, null=True)
    device = models.ForeignKey(Device)
    
    def display(self):
        # capture_time = format(self.time, u'U')
        capture_time = (time.mktime(self.time.timetuple())*1000)
        return int(capture_time) , self.value 
    
    def val(self):
        return self.value
    def tps(self):
        return self.time


class D_agregation(models.Model):
    SENSOR_TYPES = (
        ('temp', 'Temperature'),
        ('presence', 'Presence'),
    )
    time = models.DateTimeField()
    sensor_type = models.CharField(max_length=8, choices=SENSOR_TYPES)
    
    value = models.FloatField(blank=True, default=None, null=True)
    device = models.ForeignKey(Device)
    
    def display(self):
        # capture_time = format(self.time, u'U')
        capture_time = (time.mktime(self.time.timetuple())*1000)
        return int(capture_time) , self.value
    
    def val(self):
        return self.value
    def tps(self):
        return self.time
    
    
class M_agregation(models.Model):
    SENSOR_TYPES = (
        ('temp', 'Temperature'),
        ('presence', 'Presence'),
    )
    time = models.DateTimeField()
    sensor_type = models.CharField(max_length=8, choices=SENSOR_TYPES)
    
    value = models.FloatField(blank=True, default=None, null=True)
    device = models.ForeignKey(Device)
    
    def display(self):
        # capture_time = format(self.time, u'U')
        capture_time = (time.mktime(self.time.timetuple())*1000)
        return int(capture_time) , self.value
    
    def val(self):
        return self.value
    def tps(self):
        return self.time
    
    
class Y_agregation(models.Model):
    SENSOR_TYPES = (
        ('temp', 'Temperature'),
        ('presence', 'Presence'),
    )
    time = models.DateTimeField()
    sensor_type = models.CharField(max_length=8, choices=SENSOR_TYPES)
    
    value = models.FloatField(blank=True, default=None, null=True)
    device = models.ForeignKey(Device)
    
    def display(self):
        # capture_time = format(self.time, u'U')
        capture_time = (time.mktime(self.time.timetuple())*1000)
        return int(capture_time) , self.value
    
    def val(self):
        return self.value
    def tps(self):
        return self.time
    
    
class LoginForm(forms.Form):
    username = forms.CharField(required = True)
    password = forms.PasswordInput(render_value = True)



