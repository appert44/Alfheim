# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.template.context import RequestContext
from django import forms
from django.db import models


class Login(TemplateView):
    template_name = "alfheimweb/login.html"
    
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
