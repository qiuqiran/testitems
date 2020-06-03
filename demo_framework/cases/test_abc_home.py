#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
import requests
from demo_framework.framework.base import Base,Request
import datetime


class home(unittest.TestCase):
    '''XXXX'''

    def setUp(self):

        #获取公共接口地址
        self.base = Base()
        self.url = self.base.url()

        #当前测试接口地址
        print('测试开始')

    def tearDown(self):
        print('测试结束')

    def test_01(self):
        ''' XXX '''
        print('用例1',self.url)

    def test_02_get(self):
        ''' XXX '''
        print('用例get')
        # self.assertEqual('d',1)
        url = "https://sit.zooming-data.com/helper-rest/miniapp/common/allCity"
        a = "eyJhbGciOiJIUzUxMiJ9.eyJyYW5kb21LZXkiOiIxZTdtcGciLCJzdWIiOiJjbGllbnRJZDp3eDZjNjQyM2M5ZWZiNDRjNzU6NjQ3IiwiZXhwIjoxNTUzNDk3MjQ5LCJpYXQiOjE1NTI4OTI0NDl9.EGbdTfLsseGgkzOsDF99Ueklgm9tnNodk_hzeMZ24qXSejNOwPT0_qO5BsvllvDiuVrEjDadDaNk-t06YZTJlw"
        headers = {'Authorization': a,'appId': "wx6c6423c9efb44c75"}
        params =""

        # get 请求
        Request().get(url,headers,params)

    def test_03_post(self):
        '''post请求'''
        print('用例post')

        url = "https://sit.zooming-data.com/helper-rest/miniapp/linker/collection/insert"
        a = "eyJhbGciOiJIUzUxMiJ9.eyJyYW5kb21LZXkiOiIxZTdtcGciLCJzdWIiOiJjbGllbnRJZDp3eDZjNjQyM2M5ZWZiNDRjNzU6NjQ3IiwiZXhwIjoxNTUzNDk3MjQ5LCJpYXQiOjE1NTI4OTI0NDl9.EGbdTfLsseGgkzOsDF99Ueklgm9tnNodk_hzeMZ24qXSejNOwPT0_qO5BsvllvDiuVrEjDadDaNk-t06YZTJlw"
        headers = {'Authorization': a,'appId': "wx6c6423c9efb44c75"}
        params ={"clientId":647,"agentId":4477,"linkerId":"1ed4925a79ca4ce5b697784579b994e5"}

        # post 请求
        a = Request().post(url,headers,params)
        print(a.text)

    def test_04_post_json(self):
        print('用例post_json')

        url = "https://sit.zooming-data.com/helper-rest/miniapp/common/data/report"
        a = "eyJhbGciOiJIUzUxMiJ9.eyJyYW5kb21LZXkiOiIxZTdtcGciLCJzdWIiOiJjbGllbnRJZDp3eDZjNjQyM2M5ZWZiNDRjNzU6NjQ3IiwiZXhwIjoxNTUzNDk3MjQ5LCJpYXQiOjE1NTI4OTI0NDl9.EGbdTfLsseGgkzOsDF99Ueklgm9tnNodk_hzeMZ24qXSejNOwPT0_qO5BsvllvDiuVrEjDadDaNk-t06YZTJlw"
        headers = {'Authorization': a,'appId': "wx6c6423c9efb44c75",'Content-Type': "application/json"}
        for i in (647,667):
            now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            params ={
                    "clientId": i,
                    "clientName": "Qiukerosmf",
                    "action": "",
                    "agentId": 0,
                    "city": "",
                    "district": "",
                    "houseId": "",
                    "houseName": "",
                    "houseType": "",
                    "houseTypePriceAVG": 0,
                    "houseTypePriceMax": 0,
                    "houseTypePriceMin": 0,
                    "houseTypeSizeMax": 0,
                    "houseTypeSizeMin": 0,
                    "userActionCode": "SYCSXZ",
                    "userActionData": "",
                    "userActionType": "viewHouse",
                    "location": "",
                    "longitude": 113.932945,
                    "latitude": 22.52553,
                    "articleId": 0,
                    "articleTitle": "",
                    "viewTime": now
                }

            # post 请求
            a = Request().post_json(url,headers,params)
            print(a.text)




if __name__=='__main__':
    unittest.main()