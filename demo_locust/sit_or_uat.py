#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
用于切换sit环境和uat环境，根据需要的环境切换即可：

-------------------切换sit--------------------------------
    ... define your tests ...
    if __name__=='__main__':
        # 切换到sit环境
        Switching_environment().Switching_sit()
-------------------切换uat----------------------------------
    ... define your tests ...
    if __name__=='__main__':
        # 切换到uat环境
        Switching_environment().Switching_uat()
-------------------------------------------------------------
运行前先确认写入那个环境，例如写入uat，需要if __name__=='__main__':注释sit写入语句

'''

__author__ = "qiu qi ran"
__version__ = "0.3.0"

'''
Change History

Version 0.3.0
* 修改压力测试相关参数.

Version 0.2.0
* 修改获取token方法.

Version 0.1.0
* 补全sit参数/uat参数.

'''

import os
import configparser
import time
import requests


class Switching_environment():
    '''
    修改环境参数，运行自动写入config.ini
    '''


    def Switching_sit(self):
        '''sit的环境变量'''

        # 获取当前路径
        d = os.path.dirname(__file__)
        # 拼接配置文件地址
        file_path = d + '/config.ini'

        # 配置文件连接
        config = configparser.ConfigParser()
        # 读取配置文件
        config.read(file_path)

        # 相关参数
        agentid = 1001604
        corpid = 'ww8f6801ba5fd2a112'
        linkerId = '43d3c9579ce24215b1fe93dc38efffa9' # 太子湾. 湾玺一号

        # 修改mysql----------------------------------------
        config.set('mysqlconf', 'host', '111.230.195.67')
        config.set('mysqlconf', 'port', '3309')
        config.set('mysqlconf', 'user', 'tester')
        config.set('mysqlconf', 'password', 'fGh5atKr2yJ5RM1M')
        config.set('mysqlconf', 'db_name', 'aw_sit_90')
        # 修改测试地址--------------------------------------
        config.set('testServer', 'qywx_url', 'https://sit.zooming-data.com/helper-rest/qywx')
        config.set('testServer', 'api_url', 'https://sit.zooming-data.com/dist-admin')
        # 修改账号参数--------------------------------------
        config.set('qywxconfig', 'agentid', '%s'% agentid)
        config.set('qywxconfig', 'mobile', '15622518977')
        config.set('qywxconfig', 'corpid', '%s' % corpid)
        config.set('qywxconfig', 'linkerId','%s' % linkerId)

        # 写入
        with open(file_path, 'w') as f:
            config.write(f)

        print('切换到sit环境')

        # 获取token---------------------------------------
        time.sleep(1)
        print('开始获取企业微信token')
        # 参数
        url2 = 'https://sit.zooming-data.com/helper-rest/qywx/cp/oauth2/getToken'
        params2 = {'agentId': agentid, 'corpId': corpid}
        # 请求
        f2 = requests.post(url2,params2)
        qywxAuthorization = f2.json()['data']['token']

        config.set('qywxconfig', 'qywx_authorization', qywxAuthorization)
        # 写入
        with open(file_path, 'w') as f:
            config.write(f)


    def Switching_uat(self):
        '''uat的环境变量'''

        # 获取当前路径
        d = os.path.dirname(__file__)

        # 拼接配置文件地址
        file_path = d + '/config.ini'

        # 配置文件连接
        config = configparser.ConfigParser()
        # 读取配置文件
        config.read(file_path)

        # 相关参数
        # agentid = 10495
        agentid = 10702
        corpid = 'ww5eeb7240bcbad28a'
        linkerId = '846e39ce2afc4556a2751f223d67b241'  # 太子湾. 湾玺一号

        # 修改mysql----------------------------------------
        config.set('mysqlconf', 'host', '111.230.195.67')
        config.set('mysqlconf', 'port', '3306')
        config.set('mysqlconf', 'user', 'test_group')
        config.set('mysqlconf', 'password', 'nO1uC5ptK5sthrF')
        config.set('mysqlconf', 'db_name', 'ljq_helper_91')

        # 修改测试地址--------------------------------------
        config.set('testServer', 'qywx_url', 'https://uat.zooming-data.com/helper-rest/qywx')
        config.set('testServer', 'api_url', 'https://uat.zooming-data.com/dist-admin')

        # 修改账号参数--------------------------------------
        config.set('qywxconfig', 'agentid', '%s' % agentid)
        config.set('qywxconfig', 'mobile', '15622518977')
        config.set('qywxconfig', 'corpid', '%s' % corpid)
        config.set('qywxconfig', 'linkerId', '%s' % linkerId)

        # 写入
        with open(file_path, 'w') as f:
            config.write(f)

        print('切换到uat环境')

        # 获取token---------------------------------------
        time.sleep(1)
        print('开始获取企业微信token')
        # 参数
        url2 = 'https://uat.zooming-data.com/helper-rest/qywx/cp/oauth2/getToken'
        params2 = {'agentId': agentid, 'corpId': corpid}
        # 请求
        f2 = requests.post(url2, params2)
        qywxAuthorization = f2.json()['data']['token']

        config.set('qywxconfig', 'qywx_authorization', qywxAuthorization)
        # 写入
        with open(file_path, 'w') as f:
            config.write(f)


    def Switching_online(self):
        '''online的环境变量'''

        # 获取当前路径
        d = os.path.dirname(__file__)

        # 拼接配置文件地址
        file_path = d + '/config.ini'

        # 配置文件连接
        config = configparser.ConfigParser()
        # 读取配置文件
        config.read(file_path)

        # 相关参数
        agentid = 8719
        corpid = 'ww5da6447305627eb1'
        linkerId = 'accdd58b84d2426c86621ab2118d8215'  # 邱楼盘一号

        # 修改mysql----------------------------------------
        config.set('mysqlconf', 'host', '111.230.195.67')
        config.set('mysqlconf', 'port', '3307')
        config.set('mysqlconf', 'user', 'developer')
        config.set('mysqlconf', 'password', 'VF\9@;a"7n3JSh<')
        config.set('mysqlconf', 'db_name', 'ljq_helper_91')

        # 修改测试地址--------------------------------------
        config.set('testServer', 'qywx_url', 'https://helper.zooming-data.com/helper-rest/qywx')
        config.set('testServer', 'api_url', 'https://helper.zooming-data.com/dist-admin')

        # 修改账号参数--------------------------------------
        config.set('qywxconfig', 'agentid', '%s' % agentid)
        config.set('qywxconfig', 'mobile', '15622518977')
        config.set('qywxconfig', 'corpid', '%s' % corpid)
        config.set('qywxconfig', 'linkerId', '%s' % linkerId)

        # 写入
        with open(file_path, 'w') as f:
            config.write(f)

        print('切换到生产环境')

        # 获取token---------------------------------------
        time.sleep(1)
        print('开始获取企业微信token')
        # 参数
        url2 = 'https://helper.zooming-data.com/helper-rest/qywx/cp/oauth2/getToken'
        params2 = {'agentId': agentid, 'corpId': corpid}
        # 请求
        f2 = requests.post(url2, params2)
        qywxAuthorization = f2.json()['data']['token']

        config.set('qywxconfig', 'qywx_authorization', qywxAuthorization)
        # 写入
        with open(file_path, 'w') as f:
            config.write(f)


if __name__=='__main__':
    #################################################################
    # 切换环境记得注释另一个环境的语句
    #################################################################

    # 切换到sit环境
    # Switching_environment().Switching_sit()
    # 切换到uat环境
    Switching_environment().Switching_uat()
    # 切换到online环境
    # Switching_environment().Switching_online()


