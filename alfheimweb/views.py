# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.template.context import RequestContext
from django import forms
from django.db import models
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from raven.contrib.django.models import client


class Login(TemplateView):
    template_name = "alfheimweb/login.html"

def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            auth_login(request, user)
            return render_to_response('alfheimweb/main.html',context_instance=RequestContext(request))
        else:
            return HttpResponse('Compte inactif.')
    else:
        return HttpResponse('Compte non reconnu.') 

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

    Capture = models.get_model('alfheimweb', 'Capture')
    instance = Capture.objects.create(**data)
    #instance = Capture.objects.create(
    #    time = data['time'],
    #   ...
    #)
    return HttpResponse(status=201, content=instance.id)


