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
            return render_to_response('alfheimweb/main.html' ,context_instance=RequestContext(request))
        else:
            return HttpResponse('Compte inactif.')
    else:
        return render_to_response('alfheimweb/unknown.html')
     
def get_graph(request):

    data = list()
    for capture in TableBrut.objects.all().order_by('time'):
        data.append(capture.display())
    #result = [{'label': u"température intérieure", 'data': data}]
    result = {'label': u"température intérieure", 'data': data}
    # print(output)
    return HttpResponse(json.dumps(result), content_type="application/json")

def get_sensors(request):
    sensors_user = list ()
    for device in Device.objects.all():
        sensors_user.append(device.display())
    result = [{'label': "66", 'data': sensors_user}]
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

class Agregation(CronJobBase):
    RUN_AT_TIMES = ['00:02', '01:09', '02:02', '03:02', '04:02', '05:02', '06:02', '07:02', '08:02', '09:02', '10:02']
    def h_agrege(self):
        if H_agregation.objects.count() == 0:
            for lastline in TableBrut.objects.all().order_by('time'):
                lasttps = lastline.tps()
            H_startTime= datetime.datetime(lasttps.year, lasttps.month, lasttps.day, lasttps.hour, 00, 00)
            H_endTime= datetime.datetime(lasttps.year, lasttps.month, lasttps.day, lasttps.hour, 59, 59)
        else:
            for lastline in H_agregation.objects.all().order_by('time'):
                lasttps = lastline.tps()
            H_startTime= datetime.datetime(lasttps.year, lasttps.month, lasttps.day, lasttps.hour, 00, 00)
            H_endTime= datetime.datetime(lasttps.year, lasttps.month, lasttps.day, lasttps.hour, 59, 59)
        h_agrega = 0
  #  for testtablebrut in TableBrut.objects.get(time >= H_startTime | time <= H_endTime):
    #for h_create in TableBrut.objects.filter(time =[Q(H_startTime), Q(H_endTime)]):
        for h_create in TableBrut.objects.filter(Q(time__gte=H_startTime) | Q(time__lte=H_endTime)):
            h_agrega = h_agrega + h_create.val()
        h_nbrow = TableBrut.objects.count()
        h_final = h_agrega / h_nbrow
        H_agregation.objects.create(time=H_startTime, value=h_final,device_id="001",sensor_type="temp")

    schedule = Schedule(run_at_times=RUN_AT_TIMES)       
    
    
    
    







    
