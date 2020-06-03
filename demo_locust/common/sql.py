#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from common.base import Base
import requests
import json
import time

class aw_sql:
    db = Base().mysql_connect()
    id = Base().agentId()
    db_name = Base().db_name()
    token = Base().qywx_authorization()
    agentId = Base().agentId()

    def payOpenid(self,agentId):
        '''
        payOpenid
        :return:
        '''
        # 创建游标
        cursor = self.db.cursor()
        sql = "SELECT pay_open_id FROM `helper_user` WHERE id='%s';"%agentId
        cursor.execute(sql)
        payOpenid = cursor.fetchone()[0]
        print('payOpenid',payOpenid)
        return payOpenid

    def all_linker(self):
        '''
        获取全部上架楼盘
        :return:
        '''
        # 创建游标
        cursor = self.db.cursor()

        # 获取全部楼盘
        sql = "SELECT id,object_name FROM `linker_h5_720_object` WHERE del_flag=1 AND shelf_flag=0;"
        cursor.execute(sql)
        all_linker_data_num = cursor.fetchall()
        print('总楼盘数量', len(all_linker_data_num))
        return all_linker_data_num

    def amountId(self,linkerId):
        '''
        获取支付的时间和金额
        :return:
        '''
        url = Base().qywx_baseurl() + "/linkerAmount/getLinkerAmountList"
        headers = {'Authorization': self.token}
        params = {"linkerId":linkerId }
        s = requests.get(url, params=params, headers=headers)
        print(s.json()['data'][1]['id'])
        return s.json()['data'][1]['id']

    def payment(self):
        '''
        余额开通楼盘
        :return:
        '''
        url = Base().qywx_baseurl() +'/weixinPay/payment'
        payOpenid = self.payOpenid(self.agentId)
        all_linker = self.all_linker()

        for i in all_linker[0:3000]:
            print(i)
            amountId = self.amountId(i[0])
            headers = {'Authorization': self.token, 'Content-Type': 'application/json'}
            paymentReqVO = {
                        "linkerId": i[0],
                        "linkerName": i[1],
                        "costType": 2,
                        "subscribeNum": 1,
                        "amountId": amountId,
                        "payOpenid": payOpenid,
                        "channelId": ""
                    }
            r = requests.post(url, data=json.dumps(paymentReqVO), headers=headers)
            print(r.json())


        # 查看我开通了多少楼盘-----------------------------------------------------
        time.sleep(2)
        sql2 = "SELECT * FROM helper_720_project WHERE subscribe_user_id = '%s';" % self.agentId
        cursor = self.db.cursor()
        cursor.execute(sql2)
        data2 = cursor.fetchall()
        print(self.agentId,'用户开通了楼盘',len(data2),'个')

    def updateAgentStatus(self,agentId):
        '''
        更新金额
        :return:
        '''
        # 登录
        token_url = Base().api_baseurl() +"/api/login"
        token_headers = {'Content-Type': 'application/json'}
        userRq = {"account": "admin","password": "111111"}
        token_r = requests.post(token_url,data=json.dumps(userRq), headers=token_headers)
        api_token = token_r.json()['data']['userToken']['token']

        # 更新余额
        url = Base().api_baseurl() +  "/api/management/agent/updateAgentStatus"
        headers = {'Authorization': api_token, 'Content-Type': 'application/json'}
        rq = {
              "agentIds":agentId,
              "price": 500000,
            }
        r = requests.post(url, data=json.dumps(rq), headers=headers)
        print(r.json())












aw_sql().payment()