# AW大师性能测试框架

> 基于Python + Locust 的性能测试框架。
>
> 编写人：邱麒燃
>
> 时间 2019-7-16



## 使用流程

1. 运行切换环境文件
2. 进入locustfiles找到需要压测的页面接口文件，运行命令行locust -f xxx.py
3. 打开<http://localhost:8089/>编辑测试指标
4. 链接服务器查看相关指标
5. 导出需要的测试数据

## 切换环境

> sit环境运行，sit_or_uat.py运行 Switching_environment().Switching_sit()，自动获取token并写入sit环境到config.ini
>

## 数据准备

> 需要有大量数据的账号，批量开通楼盘语句



## 依赖库

> 需要安装以下内容

#### 1. Python 3.0+

```
安装python包
```

#### 2. Locustio

```python
pip install locustio
```

#### 3. PyMySQL

```python
pip install PyMySQL
```

#### 4. Pymongo

```python
pip install pymongo
```



## 架构说明

> AW_Locust 框架

* common 公共类

* locustfiles 页面接口文件

  * qywx 企业微信页面接口文件
  * miniapp 小程序页面接口文件

* md 说明文档

* report 报告文档

* config.ini 配置文件

* sit_or_uat.py 切换配置环境文件

  

