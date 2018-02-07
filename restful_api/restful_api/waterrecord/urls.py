# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^waterrecords/$', views.water_record_list, name='water_record_list'),
    # url(r'^waterrecords/$', views.WaterRecordList.as_view(), name='water_record_list'),
    # url(r'^waterrecords/$', views.WaterRecordListCreate.as_view(), name='water_record_list'),
    url(r'^waterrecords/(?P<pk>[0-9]+)$', views.water_record_detail, name='water_record_detail'),
]