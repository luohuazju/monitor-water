# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class WaterRecord(models.Model):
    waterName = models.CharField('water_name', max_length=50)
    released = models.BooleanField('released', default = False)
    releasedDate = models.CharField('released_date', max_length=20) #2018-01-16
    updateTime = models.DateTimeField('update_time', auto_now=True)
    createTime = models.DateTimeField('create_time', auto_now_add=True)

    def __unicode__(self):
        return self.waterName + self.releasedDate
