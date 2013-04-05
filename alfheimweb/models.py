# -*- coding: utf-8 -*-
from django.db import models
from django import forms
from django.forms import ModelForm, PasswordInput
from raven.contrib.django.models import client
from django.utils.dateformat import format
import datetime


class Capture(models.Model):
    SENSOR_TYPES = (
        ('temp', 'Temperature'),
        ('presence', 'Presence'),
    )
    time = models.DateTimeField()
    sensor_type = models.CharField(max_length=8, choices=SENSOR_TYPES)
    device_sn = models.CharField(max_length=45)
    value = models.FloatField(blank=True, default=None, null=True)
    
    def display(self):
        time= format(self.time, u'U')
        return u'[{0}, {1}],'.format(time, self.value)
    class Meta:
        ordering = ['-time', ]

#sclass Graph_Param_From(forms.Form):
#    number_of_measure = forms.IntegerField(300, 2, label='Number of measures (2..300)', initial = 24)
#    sensor_choice = forms.ModelChoiceField(queryset=Sensor.object.all(), required=True, label = 'Sensor')
        
class LoginForm(forms.Form):
    username = forms.CharField(required = True)
    password = forms.PasswordInput(render_value = True)
