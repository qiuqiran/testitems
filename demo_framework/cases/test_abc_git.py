#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
import requests
from demo_framework.framework.base import Base



class git(unittest.TestCase):
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

    def test_02(self):
        ''' XXX '''
        import time
        # time.sleep(5)
        print('用例2',self.url)
        # self.assertEqual('d',1)


if __name__=='__main__':
    unittest.main()