from django_cron import CronJobBase, Schedule
from django.db import models
from django.db.models import Q
from alfheimweb.models import *
from django.http import HttpResponse
import datetime

def Agregation(self):
#### agregation Hour
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
##### agregation Day
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
    D_agrega = 0

    for D_create in H_agregation.objects.filter(Q(time__gte=D_startTime) | Q(time__lte=D_endTime)):
        D_agrega = D_agrega + D_create.val()

    D_nbrow = H_agregation.objects.count()
    D_final = D_agrega / D_nbrow
    D_agregation.objects.create(time=D_startTime, value=D_final,device_id="001",sensor_type="temp")
    
##### agregation Month
    M_startTime = None
    M_endTime = None
    
    if M_agregation.objects.count() == 0:
        for M_lastline in D_agregation.objects.all().order_by('time'):
            M_lasttps = M_lastline.tps()
        M_startTime= datetime.datetime(M_lasttps.year, M_lasttps.month, M_lasttps.day, M_lasttps.hour, 00, 00)
        M_endTime= datetime.datetime(M_lasttps.year, M_lasttps.month, M_lasttps.day, M_lasttps.hour, 59, 59)
    else:
        for M_lastline in M_agregation.objects.all().order_by('time'):
            M_lasttps = M_lastline.tps()
        M_startTime= datetime.datetime(M_lasttps.year, M_lasttps.month, M_lasttps.day, M_lasttps.hour, 00, 00)
        M_endTime= datetime.datetime(M_lasttps.year, M_lasttps.month, M_lasttps.day, M_lasttps.hour, 59, 59)
    M_agrega = 0

    for M_create in D_agregation.objects.filter(Q(time__gte=M_startTime) | Q(time__lte=M_endTime)):
        M_agrega = M_agrega + M_create.val()

    M_nbrow = D_agregation.objects.count()
    M_final = M_agrega / M_nbrow
    M_agregation.objects.create(time=M_startTime, value=M_final,device_id="001",sensor_type="temp")
    
##### agregation Year
    Y_startTime = None
    Y_endTime = None
    
    if Y_agregation.objects.count() == 0:
        for Y_lastline in M_agregation.objects.all().order_by('time'):
            Y_lasttps = Y_lastline.tps()
        Y_startTime= datetime.datetime(Y_lasttps.year, Y_lasttps.month, Y_lasttps.day, Y_lasttps.hour, 00, 00)
        Y_endTime= datetime.datetime(Y_lasttps.year, Y_lasttps.month, Y_lasttps.day, Y_lasttps.hour, 59, 59)
    else:
        for Y_lastline in Y_agregation.objects.all().order_by('time'):
            Y_lasttps = Y_lastline.tps()
        Y_startTime= datetime.datetime(Y_lasttps.year, Y_lasttps.month, Y_lasttps.day, Y_lasttps.hour, 00, 00)
        Y_endTime= datetime.datetime(Y_lasttps.year, Y_lasttps.month, Y_lasttps.day, Y_lasttps.hour, 59, 59)
    
    Y_agrega = 0

    for Y_create in M_agregation.objects.filter(Q(time__gte=Y_startTime) | Q(time__lte=Y_endTime)):
        Y_agrega = Y_agrega + Y_create.val()

    Y_nbrow = M_agregation.objects.count()
    Y_final = Y_agrega / Y_nbrow
    Y_agregation.objects.create(time=Y_startTime, value=Y_final,device_id="001",sensor_type="temp")
