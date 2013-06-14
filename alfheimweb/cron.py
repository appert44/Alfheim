from django_cron import CronJobBase, Schedule
from django.db import models
from django.db.models import Q
from alfheimweb.models import *
from django.http import HttpResponse
from datetime import datetime    
import datetime

def Agregation(self):
    
    h = 0
    d = 0
    
    date = datetime.datetime.now()

    while h < 24:
        h_prec_agrega = 0
        h_temp_agrega = 0
        H_startTime= datetime.datetime(date.year, date.month, (date.day-1), h, 00, 00)
        H_endTime= datetime.datetime(date.year, date.month, (date.day-1), h, 59, 59)
        #recherche des valeurs suivant les parametres 
        for h_create in TableBrut.objects.filter(Q(time__gte=H_startTime), Q(time__lte=H_endTime), Q(sensor_type="temp")):
            h_temp_agrega = h_temp_agrega + h_create.val()
        for h_create in TableBrut.objects.filter(Q(time__gte=H_startTime), Q(time__lte=H_endTime), Q(sensor_type="presence")):
            h_prec_agrega = h_prec_agrega + h_create.val()    
            
        h_temp_nbrow = TableBrut.objects.filter(Q(time__gte=H_startTime), Q(time__lte=H_endTime), Q(sensor_type="temp")).count()
        h_prec_nbrow = TableBrut.objects.filter(Q(time__gte=H_startTime), Q(time__lte=H_endTime), Q(sensor_type="presence")).count()

        if h_temp_nbrow == 0:
            h_temp_final = 0
        else:
            h_temp_final = h_temp_agrega / h_temp_nbrow
        if h_prec_agrega == 0:
            h_prec_final = 0
        else:
            h_prec_final = h_prec_agrega / h_prec_nbrow
        H_agregation.objects.create(time=H_startTime, value=h_temp_final,device_id="001",sensor_type="temp")
        H_agregation.objects.create(time=H_startTime, value=h_prec_final,device_id="001",sensor_type="presence")
        h = h + 1
        
 
    d_temp_agrega = 0
    d_prec_agrega = 0
    d_startTime= datetime.datetime(date.year, date.month, (date.day-1), 00, 00, 00)
    d_endTime= datetime.datetime(date.year, date.month, (date.day-1), 23, 59, 59) 

    for d_create in TableBrut.objects.filter(Q(time__gte=d_startTime), Q(time__lte=d_endTime), Q(sensor_type="temp")):
        d_temp_agrega = d_temp_agrega + d_create.val()
    for d_create in TableBrut.objects.filter(Q(time__gte=d_startTime), Q(time__lte=d_endTime), Q(sensor_type="presence")):
        d_temp_agrega = d_temp_agrega + d_create.val()    
            
    d_temp_nbrow = TableBrut.objects.filter(Q(time__gte=d_startTime), Q(time__lte=d_endTime), Q(sensor_type="temp")).count()
        d_prec_nbrow = TableBrut.objects.filter(Q(time__gte=d_startTime), Q(time__lte=d_endTime), Q(sensor_type="presence")).count()

def Agregation_sec(self):
    for capteur_list in TableBrut.objects.filter(Q(sensor_type="temp")):
        date = datetime.datetime(capteur_list.tps().year, capteur_list.tps().month, capteur_list.tps().day, capteur_list.tps().hour, 00, 00)
        agregation = H_agregation.object.filter()
        
    return HttpResponse(date)
    
    
    
    
