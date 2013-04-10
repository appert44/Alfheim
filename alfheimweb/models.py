from django.db import models
from django.conf import settings
from django import forms
from django.forms import ModelForm, PasswordInput
from raven.contrib.django.models import client
from django.utils.dateformat import format
from django.contrib.auth.models import User
import datetime


class Capture(models.Model):
    SENSOR_TYPES = (
        ('temp', 'Temperature'),
        ('presence', 'Presence'),
    )
    #username = models.ForeignKey(User)
    time = models.DateTimeField()
    sensor_type = models.CharField(max_length=8, choices=SENSOR_TYPES)
    device_sn = models.CharField(max_length=45)
    value = models.FloatField(blank=True, default=None, null=True)
    
    def display(self):
        time= format(self.time, u'U')
        return u'[{0}, {1}],'.format(time, self.value)
    class Meta:
        ordering = ['-time', ]
        
class LoginForm(forms.Form):
    username = forms.CharField(required = True)
    password = forms.PasswordInput(render_value = True)