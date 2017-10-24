"""
Author: Abhishek
Description: This file is not a default file. We have to create this file for each django app.

"""
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]

