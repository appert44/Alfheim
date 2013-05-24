from django_cron import CronJobBase, Schedule
from django.db import models
from django.db.models import Q
from alfheimweb.models import *
import datetime

def Agregation():
##### agrégation Hour
    H_startTime = None
    H_endTime = None
    
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

    for h_create in TableBrut.objects.filter(Q(time__gte=H_startTime) | Q(time__lte=H_endTime)):
        h_agrega = h_agrega + h_create.val()
    h_nbrow = TableBrut.objects.count()
    h_final = h_agrega / h_nbrow
    H_agregation.objects.create(time=H_startTime, value=h_final,device_id="001",sensor_type="temp")
##### agrégation Day
    D_startTime = None
    D_endTime = None
    
    if D_agregation.objects.count() == 0:
        for D_lastline in H_agregation.objects.all().order_by('time'):
            D_lasttps = D_lastline.tps()
        D_startTime= datetime.datetime(D_lasttps.year, D_lasttps.month, D_lasttps.day, D_lasttps.hour, 00, 00)
        D_endTime= datetime.datetime(D_lasttps.year, D_lasttps.month, D_lasttps.day, D_lasttps.hour, 59, 59)
    else:
        for D_lastline in D_agregation.objects.all().order_by('time'):
            D_lasttps = D_lastline.tps()
        D_startTime= datetime.datetime(D_lasttps.year, D_lasttps.month, D_lasttps.day, D_lasttps.hour, 00, 00)
        D_endTime= datetime.datetime(D_lasttps.year, D_lasttps.month, D_lasttps.day, D_lasttps.hour, 59, 59)
    h_agrega = 0

    for D_create in H_agregation.objects.filter(Q(time__gte=D_startTime) | Q(time__lte=D_endTime)):
        D_agrega = D_agrega + D_create.val()
    D_nbrow = H_agregation.objects.count()
    D_final = D_agrega / D_nbrow
    D_agregation.objects.create(time=D_startTime, value=D_final,device_id="001",sensor_type="temp")