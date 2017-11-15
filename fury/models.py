# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class nse_bhav_staging(models.Model):
	pass


class Portfolio(models.Model):
	stock = models.CharField(max_length=200)
	shares = models.IntegerField()
	notes = models.CharField(max_length=200)
	price = models.FloatField()
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	added_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	
	def __str__(self): 
		return self.stock

