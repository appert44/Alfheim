# -*- coding: utf-8 -*-
from django.db import models
from django import forms
from django.forms import ModelForm, PasswordInput
from raven.contrib.django.models import client
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

    class Meta:
        ordering = ['-time', ]
        
class LoginForm(forms.Form):
    username = forms.CharField(required = True)
    password = forms.PasswordInput(render_value = True)
