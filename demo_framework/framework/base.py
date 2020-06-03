#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
用于Python单元测试框架的公共类运行程序。
读取根目录config.ini配置文件，返回公共变量。
'''

__author__ = "qiu qi ran"
__version__ = "0.1.2"


import configparser
import os
import requests
import json
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
import time
from selenium import webdriver


#------读取配置文件-----------

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
URL = config.get('testServer', 'url')

#----------------------------


class Base:
    '''公共变量'''

    def url(self):
        '''测试地址'''

        self.url  = URL
        return self.url

    def venv(self):
        '''判断在哪个环境'''
        if URL== 'https://www.baidu.com/':
            venv = 'baidu'
            return venv
        elif URL== 'https://www.sogou.com/':
            venv = 'sogou'
            return venv
        else:
            venv = 'baidu'
            return venv


    def send_email(self, filename, png, venv):
        '''发送邮件'''
        # --------填写邮箱信息-----
        me_email = '2167598@163.com'
        me_pass = 'qiuqiran123456'
        kew = '404657468@qq.com'
        kew2 = 'qiuqiran@gmail.com'

        # -----发送信息-----
        msg = MIMEMultipart()  # 附件
        msg['From'] = formataddr(["qiuqiran", me_email])
        msg['To'] = formataddr(["", kew])
        msg['Subject'] = venv + "接口自动化测试报告"

        # ----------正文-------
        view = """
<body>
<table width=100% border="1" cellspacing="0" cellpadding="4">
<tr>
    <td bgcolor="#CECFAD" height="20" style="font-size:14px">自动化测试报告</a></td>
</tr>
<tr>
    <td bgcolor="#EFEBDE" height="100" style="font-size:13px">
        1、图片png：为测试报告预览。<br>
        2、附件html：为测试报告详细文档 <br>
        3、查看详细请下载附件操作 <br>
    </td>
</tr>
</table>
"""
        text_plain = MIMEText(view, 'html', 'utf-8')
        msg.attach(text_plain)
        # ----------图片----------
        sendimagefile = open(png, 'rb').read()
        image = MIMEImage(sendimagefile)
        image.add_header('Content-ID', '<image1>')
        image["Content-Disposition"] = 'attachment; filename="testimage.png"'
        msg.attach(image)
        # ----------附件----------
        aaa = MIMEText(open(filename, 'rb').read(), 'base64', 'utf-8')
        aaa["Content-Type"] = 'application/octet-stream'
        aaa["Content-Disposition"] = 'attachment; filename="test_report.html"'
        msg.attach(aaa)

        # ----------发送------------
        try:
            server = smtplib.SMTP_SSL("smtp.163.com", 465)
            server.login(me_email, me_pass)
            server.sendmail(me_email, [kew, kew2, ], msg.as_string())
            server.quit()
            print('邮件发送成功')
        except smtplib.SMTPException:
            print('邮件发送失败')

    def screenshot(self,filename,png):
        '''截图'''

        option = webdriver.ChromeOptions()
        option.add_argument('headless')
        driver = webdriver.Chrome(chrome_options=option)
        driver.get(filename)
        time.sleep(2)
        driver.save_screenshot(png)
        driver.close()

class Request:
    '''接口框架'''
    def get(self,url,headers,params):
        '''get请求'''
        f = requests.get(url=url,headers=headers,params=params)
        return f

    def post(self,url,headers,params):
        '''post请求'''
        f = requests.post(url=url, headers=headers, params=params)
        return f

    def post_json(self,url,headers,params):
        '''带有json的post请求'''
        f = requests.post(url=url, data=json.dumps(params), headers=headers)
        return f

class Webdriver:
    '''ui框架'''
    def __init__(self):
        """
        写一个构造函数，有一个参数driver,启动浏览器
        :param driver:
        """
        self.driver = webdriver.Chrome()
        # self.driver = webdriver.Edge()  # Edge浏览器

    def open_url(self, url):
        """
        打开url站点
        :param url:
        """

        self.driver.get(url)

    def quit_browser(self):
        """
        关闭并停止浏览器服务
        :param none:
        """
        self.driver.quit()

    def find_element(self, selector):
        """
         这个地方为什么是根据=>来切割字符串，请看页面里定位元素的方法
         submit_btn = "id=>su"
         login_lnk = "xpath => //*[@id='u1']/a[7]"  # 百度首页登录链接定位
         如果采用等号，结果很多xpath表达式中包含一个=，这样会造成切割不准确，影响元素定位
        :param selector:
        :return: element
        """
        element = ''
        if '=>' not in selector:
            return self.driver.find_element_by_id(selector)
        selector_by = selector.split('=>')[0]
        selector_value = selector.split('=>')[1]

        if selector_by == "i" or selector_by == 'id':

            element = self.driver.find_element_by_id(selector_value)

        elif selector_by == "n" or selector_by == 'name':
            element = self.driver.find_element_by_name(selector_value)
        elif selector_by == "c" or selector_by == 'class_name':
            element = self.driver.find_element_by_class_name(selector_value)
        elif selector_by == "l" or selector_by == 'link_text':
            element = self.driver.find_element_by_link_text(selector_value)
        elif selector_by == "p" or selector_by == 'partial_link_text':
            element = self.driver.find_element_by_partial_link_text(selector_value)
        elif selector_by == "t" or selector_by == 'tag_name':
            element = self.driver.find_element_by_tag_name(selector_value)
        elif selector_by == "x" or selector_by == 'xpath':
            element = self.driver.find_element_by_xpath(selector_value)

        elif selector_by == "s" or selector_by == 'selector_selector':
            element = self.driver.find_element_by_css_selector(selector_value)
        else:
            raise NameError("Please enter a valid type of targeting elements.")

        return element


    def type(self, selector, text):

        el = self.find_element(selector)
        el.clear()
        el.send_keys(text)

    def click(self, selector):

        el = self.find_element(selector)
        el.click()


class locust:
    pass
class appmiu:
    pass