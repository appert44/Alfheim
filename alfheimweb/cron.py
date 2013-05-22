from django_cron import CronJobBase, Schedule
from django.db import models
from django.db.models import Q
from alfheimweb.models import *
import datetime

class Agregation(CronJobBase):
    RUN_AT_TIMES = ['00:02', '01:23', '02:02', '03:02', '04:02', '05:02', '06:02', '07:02', '08:02', '11:09', '11:11']
    schedule = Schedule(run_at_times=RUN_AT_TIMES) 
    ALLOW_PARALLEL_RUNS = True
    code = "alfheimweb.Agregation"
    def do(self):
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

