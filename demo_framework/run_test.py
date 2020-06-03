#!/usr/bin/env python3
# -*- coding: utf-8 -*-



__author__ = "qiu qi ran"
__version__ = "0.1.2"

'''
Change History

Version 0.1.2
* 修复动态获取路径bug

Version 0.1.1
* 添加邮件发送附件和正文

Version 0.1.0
* 修复多人右键收取问题

'''

import time
from demo_framework.framework.HTMLTestRunner import HTMLTestRunner
import unittest
import os
from demo_framework.framework.base import Base



class Run_all():
    '''
    测试主入口
    pycharm 运行即可
    '''

    def Cases_report(self):
        '''
        生产测试报告并发送邮件
        '''

        #----------查看当前在sit还是uat------
        venv = Base().venv()

        #----------指定测试用例文件-----------
        d = os.path.dirname(__file__)
        test_dir = d + '/cases/'


        #discover是递归匹配文件的，如果有子目录需要有__init__.py，
        discover = unittest.defaultTestLoader.discover(test_dir, pattern='test_*.py',top_level_dir=None)


        #-----------获取当前时间---------
        now = time.strftime('%m-%d_%H_%M')
        #-----------生成路径------------
        # filename = d + '/report/' + now + '_' + venv +'_report.html'
        filename= d + "/report/test_report.html"
        png = d + "/report/view.png"

        #-----------运行并生成报告文件---------
        fp = open(filename, 'wb')
        runner = HTMLTestRunner(stream=fp,title=venv + '接口自动化测试报告',)
        runner.run(discover)
        fp.close()

        # ----------截图预览------------------
        Base().screenshot(filename,png)

        # ----------发邮件-----------------
        Base().send_email(filename,png,venv)









if __name__=='__main__':
    Run_all().Cases_report()







