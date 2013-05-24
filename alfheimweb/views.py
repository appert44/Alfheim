# -*- coding: utf-8 -*-
from django.views.generic import TemplateView
from django.template.context import RequestContext
from django import forms
from django.db import models
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
#from django.contrib.auth import logout
from django.http import HttpResponse
from django.shortcuts import render_to_response
#from django.http import HttpResponseRedirect
#from raven.contrib.django.models import client
from BeautifulSoup import BeautifulSoup
from django import template
from alfheimweb.models import *
from django.template import Context, loader
from django.db.models import Q
from django_cron import CronJobBase, Schedule

import datetime
import json


class Login(TemplateView):
    template_name = "alfheimweb/login.html"


def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            auth_login(request, user)
            return render_to_response('alfheimweb/main.html', context_instance=RequestContext(request))
        else:
            return HttpResponse('Compte inactif.')
    else:
        return render_to_response('alfheimweb/unknown.html')


def get_graph(request):
    data = list()
    if request.method == 'GET':
        choice = request.GET.get("choice")
        if choice == 'hour':
            for capture in H_agregation.objects.all().order_by('time'):
                data.append(capture.display())
        elif choice == 'day':
            for capture in D_agregation.objects.all().order_by('time'):
                data.append(capture.display())
        elif choice == 'month':
            for capture in M_agregation.objects.all().order_by('time'):
                data.append(capture.display())
        elif choice == 'year':
            for capture in Y_agregation.objects.all().order_by('time'):
                data.append(capture.display())
        result = {'label': u"température intérieure", 'data': data}
        return HttpResponse(json.dumps(result), content_type="application/json")
    else:
        return HttpResponse(status=400)


def get_sensors(request):
    sensors_user = list()
    for device in Device.objects.all():
        sensors_user.append(device.display())
    #result = [{'label': "sensors", 'data': sensors_user}]
    result = {'data': sensors_user}
    return HttpResponse(json.dumps(result), content_type="application/json")


class Notlogged(TemplateView):
    template_name = "alfheimweb/notlogged.html"


class Main(TemplateView):
    template_name = "alfheimweb/main.html"


class MeasureForm(forms.Form):
    time = forms.DateTimeField(required=False)
    sensor_type = forms.CharField(max_length=8)
    device_sn = forms.CharField(required=False, max_length=45)
    value = forms.FloatField(required=False)


def measure(request):
    #import ipdb
    #ipdb.set_trace()
    form = MeasureForm(request.POST)
    if not form.is_valid():
        return HttpResponse(status=400, content=form.errors.as_text())
    #form is valid
    data = form.cleaned_data

    Device = models.get_model('alfheimweb', 'Device')
    device, created = Device.objects.get_or_create(serial_number=data['device_sn'])
    del data['device_sn']
    data['device'] = device
    TableBrut = models.get_model('alfheimweb', 'TableBrut')
    instance = TableBrut.objects.create(**data)
    #instance = TableBrut.objects.create(
    # time = data['time'],
    # ...
    #)
    return HttpResponse(status=201, content=instance.id)
