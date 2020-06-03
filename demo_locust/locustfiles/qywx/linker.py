#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
全部楼盘列表，涉及2个接口
'''


from locust import HttpLocust, TaskSet, task
import sys
import os
sys.path.append(os.getcwd())
import common.base


class base:
    '''
    该页面需要用到的参数
    '''

    def url(self):
        '''
        测试环境域名
        :return:
        '''
        url = common.base.Base.qywx_baseurl(self)
        return url

    def token(self):
        '''
        获取token
        :return:
        '''
        token = common.base.Base.qywx_authorization(self)
        return token


class WebsiteTasks(TaskSet):

    def brokerVip(self):
        '''
        查询vip模块
        :return:
        '''
        url = '/brokerVip/vipInfoList'
        headers = {'Authorization': base().token()}
        s = self.client.get(url, headers=headers)
        print(s.json())

    def linker(self):
        '''
        全部楼盘模块
        :return:
        '''
        url = '/linker/getLinkerList'
        headers = {'Authorization': base().token()}
        params = {"size": 10, "current": 1,"city":"全国"}
        s = self.client.get(url, params=params, headers=headers)
        print(s.json()['data']['total'])

    @task(1)
    def start(self):
        self.brokerVip()
        self.linker()

class WebsiteUser(HttpLocust):
    task_set = WebsiteTasks
    min_wait = 0
    max_wait = 1
    host = base().url()