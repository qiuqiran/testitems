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
__version__ = "0.1.0"

'''
Change History

Version 0.1.0
* 补全sit参数/uat参数.

'''

import os
import configparser
import time
from demo_framework.framework.base import Base


class Switching_environment():

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
        # 修改测试地址--------------------------------------
        config.set('testServer', 'url', 'https://www.baidu.com/')

        # 写入
        with open(file_path, 'w') as configfile:
            config.write(configfile)
        print('切换到baidu环境')


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
        # 修改测试地址--------------------------------------
        config.set('testServer', 'url', 'https://www.sogou.com/')

        # 写入
        with open(file_path, 'w') as configfile:
            config.write(configfile)
        print('切换到sogou环境')



if __name__=='__main__':
    #################################################################
    # 切换环境记得注释另一个环境的语句
    #################################################################

    Switching_environment().Switching_sit()
    # Switching_environment().Switching_uat()


