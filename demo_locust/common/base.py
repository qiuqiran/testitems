#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# 读取根目录config.ini配置文件，返回公共变量。


__author__ = "qiu qi ran"
__version__ = "0.1.1"

'''
Change History

Version 0.1.1

* 区分90和91库参数

Version 0.1.0
* 新增企业微信关联参数
* 迁移不必要的数据
* 简化公共类


'''

import configparser
import pymysql
import os
import random




################################################
#                  读取配置文件
################################################
#返回当前文件所在的目录
d = os.path.dirname(__file__)
#获得d所在的目录,即d的父级目录  + 配置文件
file_path = os.path.dirname(d)+ '/config.ini'
# print(file_path)

#实例配置文件
config = configparser.ConfigParser()
#读取配置文件
config.read(file_path)

# 获取测试地址配置
qywx_url = config.get('testServer', 'qywx_url')
api_url = config.get('testServer', 'api_url')


# 获取mysql数据库配置
host = config.get('mysqlconf', 'host')
port = config.get('mysqlconf', 'port')
user = config.get('mysqlconf', 'user')
password = config.get('mysqlconf', 'password')
db_name = config.get('mysqlconf', 'db_name')

# 获取公共变量配置
agentId = config.get('qywxconfig','agentId')
qywx_authorization = config.get('qywxconfig','qywx_authorization')
mobile = config.get('qywxconfig','mobile')
corpid = config.get('qywxconfig','corpid')
linkerId = config.get('qywxconfig','linkerId')

###############################################
#                基本类
###############################################

class Base:

    def mysql_connect(self):
        '''
        连接数据库操作
        :return:
        '''
        # 事务级别的问题，导致查询事务并没有更新,每次操作数据库后无法查询最新数据，添加autocommit = True
        self.db  = pymysql.connect(host= host, port=int(port), user= user, password= password, db=db_name, charset="utf8mb4",autocommit = True)
        return self.db

    def db_name(self):
        '''
        库名
        :return:
        '''
        self.db_name = db_name
        return self.db_name


    def qywx_baseurl(self):
        '''
        企业微信基本接口域名
        :return:
        '''
        self.qywx_baseurl = qywx_url
        return self.qywx_baseurl

    def api_baseurl(self):
        '''
        后台基本接口域名
        :return:
        '''
        self.api_baseurl = api_url
        return self.api_baseurl

    def agentId(self):
        '''
        经纪人id
        :return:
        '''
        self.agentId = agentId
        return self.agentId

    def qywx_authorization(self):
        '''
        企业微信token
        :return:
        '''
        self.qywx_authorization = qywx_authorization
        return self.qywx_authorization


    def mobile(self):
        '''
        手机号码
        :return:
        '''
        self.mobile = mobile
        return self.mobile


    def corpid(self):
        '''
        企业微信corpid
        :return:
        '''
        self.corpid = corpid
        return self.corpid


    def random_clientId(self):
        '''
        生成随机用户
        :return:
        '''
        # 查询数据库拿真实用户
        clientId_0 = range(20000,30000)
        self.random_clientId = str(random.choice(clientId_0))
        return self.random_clientId

    def linkerId(self):
        '''
        楼盘id
        :return:
        '''
        self.linkerId = linkerId
        return self.linkerId




