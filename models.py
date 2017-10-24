"""
Author: Abhishek
Description: This file is created by us by giving command 'python manage.py inspectdb > models.py'. Before issueing this command make sure you have modified setting.py file with appropriate database settings.

"""
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class NseEodStaging(models.Model):
    symbol = models.TextField(db_column='SYMBOL', blank=True, null=True)  # Field name made lowercase.
    series = models.TextField(db_column='SERIES', blank=True, null=True)  # Field name made lowercase.
    open_price = models.FloatField(db_column='OPEN_PRICE', blank=True, null=True)  # Field name made lowercase.
    high = models.FloatField(db_column='HIGH', blank=True, null=True)  # Field name made lowercase.
    low = models.FloatField(db_column='LOW', blank=True, null=True)  # Field name made lowercase.
    close = models.FloatField(db_column='CLOSE', blank=True, null=True)  # Field name made lowercase.
    last = models.FloatField(db_column='LAST', blank=True, null=True)  # Field name made lowercase.
    prevclose = models.FloatField(db_column='PREVCLOSE', blank=True, null=True)  # Field name made lowercase.
    tottrdqty = models.BigIntegerField(db_column='TOTTRDQTY', blank=True, null=True)  # Field name made lowercase.
    tottrdval = models.FloatField(db_column='TOTTRDVAL', blank=True, null=True)  # Field name made lowercase.
    timestamp = models.TextField(db_column='TIMESTAMP', blank=True, null=True)  # Field name made lowercase.
    totaltrades = models.BigIntegerField(db_column='TOTALTRADES', blank=True, null=True)  # Field name made lowercase.
    isin = models.TextField(db_column='ISIN', blank=True, null=True)  # Field name made lowercase.
    unnamed_13 = models.FloatField(db_column='Unnamed: 13', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = True
        db_table = 'nse_eod_staging'
