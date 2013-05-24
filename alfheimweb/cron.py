from django_cron import CronJobBase, Schedule
from django.db import models
from django.db.models import Q
from alfheimweb.models import *
import datetime

def Agregation():
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

