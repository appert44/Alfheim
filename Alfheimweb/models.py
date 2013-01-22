# -*- coding: utf-8- -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _

class Task(models.Model):
    content = models.CharField(_(u'task'), max_length=255)
    is_resolved = models.BooleanField(_(u'Resolved?'))

    def __unicode__(self):
        return u'Task %d : %s' % (self.id, self.content)
# Create your models here.
