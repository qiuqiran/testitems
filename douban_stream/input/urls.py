#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from django.conf.urls import url
from input import views_api

urlpatterns = [

    url(r'^s_list/', views_api.s_list,name='s_list'),#/api/s_list/
    url(r'^s_all_list/', views_api.s_all_list, name='s_all_list'),  # /api/s_all_list/
    # api/cover/
    url(r'^cover/', views_api.cover, name='cover'),  # cover接口
    url(r'^grid/', views_api.grid, name='grid'),  # grid接口


]