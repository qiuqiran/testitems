#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from django.http import JsonResponse
from input.models import Movie_list,Content
from django.core.exceptions import ValidationError
from django.core.exceptions import ValidationError, ObjectDoesNotExist
import random


def s_all_list(request):
    '''所有电影接口'''
    id = request.GET.get('id', '')

    if id == 'all':
        datas = []
        li = Movie_list.objects.all()
        for i in  li:
            list = {}
            list['id'] = i.id
            list['name'] = i.name
            list['rating_num'] = i.rating_num
            datas.append(list)
        return JsonResponse({'status': 200, 'message': 'success', 'data': datas[:2]})

    if id != 'all':
        return JsonResponse({'status': 10010, 'message': 'id cannot be empty'})


def s_list(request):
    '''查询单条电影接口'''
    id = request.GET.get('id','')

    if id == '':
        return JsonResponse({'status':10021,'message':'id  cannot be empty'})

    if id != '':
        list = {}
        try:
            result = Movie_list.objects.get(id=id)
        except ObjectDoesNotExist:
            return JsonResponse({'status': 10022, 'message': 'nothing'})
        else:
            list['name'] = result.name
            list['rating_num'] = result.rating_num
            return JsonResponse({'status': 200, 'message': 'success', 'data': list})


def short_list(request):
    '''查询短评接口'''
    id = request.GET.get('id','')

    if id == '':
        return JsonResponse({'status':10021,'message':'id  cannot be empty'})

    if id != '':
        list = {}
        try:
            result = Content.objects.get(mid_id=id)
        except ObjectDoesNotExist:
            return JsonResponse({'status': 10022, 'message': 'nothing'})
        else:
            list['name'] = result.name
            list['rating_num'] = result.rating_num
            return JsonResponse({'status': 200, 'message': 'success', 'data': list})


def cover(request):
    '''
    cover页面的接口
    :param request:
    :return:
    '''
    mid = request.GET.get('mid','')
    # realname = request.GET.get('realname','')
    # short = request.GET.get('short','')

    if mid != '':
        datas = []
        li = Content.objects.filter(mid=mid)
        # li = Content.objects.filter(mid=mid)

        for i in li:
            list = {}
            list['id'] = i.id
            list['realname'] = i.realname
            list['mid_name'] = i.mid_name
            list['short'] = i.short
            datas.append(list)


        return JsonResponse({'status': 200, 'message': 'success', 'data': datas[:1]})

    if mid == '':
        datas = []
        li = Content.objects.order_by('?')
        for i in li:
            list = {}
            list['id'] = i.id
            list['mid_name'] = i.mid_name
            list['realname'] = i.realname
            list['short'] = i.short
            datas.append(list)
        return JsonResponse({'status': 200, 'message': 'success', 'data': datas[:1]})


def grid(request):
    '''
    网格接口
    :param request:
    :return:
    '''
    mid =request.GET.get('mid','')
    datas = {'id': 192, 'mid_name': "叶问外传：张天志 葉問外傳：張天志", 'realname': "二月鸟语", 'short': "现在这些前辈还活在自己的世界里才是真的可怕······"}
    return JsonResponse({'status': 200, 'message': 'success', 'data': datas})


