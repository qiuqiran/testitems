#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
import requests
from demo_framework.framework.base import Base,Webdriver



class view(unittest.TestCase):
    '''XXXX'''

    def setUp(self):

        #获取公共接口地址
        self.base = Base()
        self.d = Webdriver()
        self.url = self.base.url()
        #当前测试接口地址
        print('测试开始')

    def tearDown(self):
        print('测试结束')
        self.d.quit_browser()

    def test_01(self):
        ''' XXX '''
        print('用例1',self.url)

    def test_02(self):
        ''' XXX '''
        print('用例2',self.url)
        self.assertEqual('d',1)

    def test_03(self):
        '''ui自动化'''
        d = self.d
        d.open_url(self.url)
        import time
        # time.sleep(1)
        d.type('x=>//*[@id="kw"]','python')
        # time.sleep(1)

        d.click('x=>//*[@id="su"]')
        time.sleep(1)

        # d.quit_browser()


if __name__=='__main__':
    unittest.main()