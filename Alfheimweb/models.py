# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
import datetime

class Task(models.Model):
    content = models.CharField(_(u'task'), max_length=255)
    is_resolved = models.BooleanField(_(u'Resolved?'))
	

    def __unicode__(self):
        return u'Task %d : %s' % (self.id, self.content)
class Capture(models.Model):
	time_stamp = models.DateTimeField(_(u'timestamp'))
	sensor_type = models.CharField(_(u'sensor_type'), max_length=45)
	sensor_serialnumber = models.CharField(_('usensor_serial'), max_length=45)
	account_id = models.IntegerField(_(u'account-id'), blank=False, null=False)
	value_temperature = models.IntegerField(_(u'value_temperature'), blank=False, null=False)
	value_presence = models.BooleanField(_(u'value_presence'), null=False, blank=False, default=False)



