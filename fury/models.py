# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class nse_bhav_staging(models.Model):

SYMBOL,SERIES,OPEN,HIGH,LOW,CLOSE,LAST,PREVCLOSE,TOTTRDQTY,TOTTRDVAL,TIMESTAMP,TOTALTRADES,ISIN,

	SYMBOL =  models.CharField(max_length=30)
	SERIES =  models.CharField(max_length=5)
	OPEN = models.DecimalField(max_digits=10, decimal_places=5)



    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
