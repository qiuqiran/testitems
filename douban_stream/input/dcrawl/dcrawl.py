#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from selenium import webdriver
from urllib import request
import re
import pymysql
from bs4 import BeautifulSoup
import sqlite3


class Douban_Crawl_data():
    '''豆瓣电影标题，评分和短评爬虫'''

    def text_01(self):
        '''sqlite3'''
        db = sqlite3.connect('main.db')  # 建立链接
        cursor = db.cursor()
        #
        # douban_id = '4920389'  # 豆瓣id
        # page_num = str(20 * 1)  # 页数
        #
        # surl = 'https://movie.douban.com/subject/' + douban_id + '/'  # 首页
        # shtml = request.urlopen(surl).read().decode('utf-8')
        # name = re.findall(r'<span property="v:itemreviewed">(.*?)</span>', shtml)  # 获取标题
        # rating_num = re.findall(r'<strong class="ll rating_num" property="v:average">(.*?)</strong>', shtml)  # 获取点评分数
        #
        # # 获取数据库id
        # sql = 'select * from input_movie_list'
        # cursor.execute(sql)
        # data = cursor.fetchall()
        # id = len(data) + 1  # 获取id
        #
        # sql1 = "INSERT INTO input_movie_list (id,name,rating_num) VALUES ('%s','%s','%s')" % (
        # id, name[0], rating_num[0])  # 写入电影表
        # cursor.execute(sql1)  # 执行语句
        # db.commit()  # 提交
        #
        # url = 'https://movie.douban.com/subject/' + douban_id + '/comments?start=' + page_num + '&limit=20&sort=new_score&status=P'  # 短评页
        # html = request.urlopen(url).read().decode('utf-8')
        # realname = re.findall(r'<a.+people.+">(.+)</a>', html)  # 用户名
        # soup = BeautifulSoup(html, 'html.parser')
        # short = soup.find_all('span', {'class': 'short'})  # 短评,换一种方法就可以获取到
        # # short = re.findall(r'<span class="short">(\S*?)</span>', html)  # 短评,第一条短评带有空格无法抓取到
        # mid = id
        #
        # a_num = 0
        # # short_new = []
        # while a_num < 20:
        #     ab = short[a_num].get_text().strip().replace("\n", "")  # 取代html标签，并且去掉豆瓣第一条短评空格换行
        #     sql2 = "INSERT INTO input_content (realname,short,mid_id) VALUES ('%s','%s','%s')" % (
        #     realname[a_num], ab, mid)  # 写入短评表
        #     cursor.execute(sql2)  # 执行语句
        #     # short_new.append(ab)
        #     db.commit()  # 提交
        #     a_num = a_num + 1




    def Douban_2(self):
        # db = pymysql.connect(host='207.246.77.150', user='root', password='2167598', db='stream', charset="utf8mb4")#建立线上数据库链接
        db = pymysql.connect(host='127.0.0.1', user='root', password='', db='stream', charset="utf8mb4")#建立本地数据库链接

        cursor = db.cursor()

        douban_id = '30212185'#豆瓣id
        page_num = str(20 * 2)#页数

        surl = 'https://movie.douban.com/subject/'+ douban_id +'/'#首页
        shtml = request.urlopen(surl).read().decode('utf-8')
        name = re.findall(r'<span property="v:itemreviewed">(.*?)</span>', shtml)  # 获取标题
        rating_num = re.findall(r'<strong class="ll rating_num" property="v:average">(.*?)</strong>', shtml)  # 获取点评分数

        # 获取数据库id
        sql = 'select * from input_movie_list'
        cursor.execute(sql)
        data = cursor.fetchall()
        id = len(data) + 1  # 获取id


        sql1 = "INSERT INTO input_movie_list (id,name,rating_num) VALUES ('%s','%s','%s')" % (id,name[0], rating_num[0])#写入电影表
        cursor.execute(sql1)  # 执行语句
        db.commit()  # 提交

        url = 'https://movie.douban.com/subject/' + douban_id + '/comments?start=' + page_num + '&limit=20&sort=new_score&status=P'#短评页
        html = request.urlopen(url).read().decode('utf-8')
        realname = re.findall(r'<a.+people.+">(.+)</a>', html)  # 用户名
        soup = BeautifulSoup(html,'html.parser')
        short = soup.find_all('span',{'class':'short'})# 短评,换一种方法就可以获取到
        # short = re.findall(r'<span class="short">(\S*?)</span>', html)  # 短评,第一条短评带有空格无法抓取到
        mid =id

        a_num = 0
        # short_new = []
        while a_num < 20:
            ab = short[a_num].get_text().strip().replace("\n", "")#取代html标签，并且去掉豆瓣第一条短评空格换行
            sql2 = "INSERT INTO input_content (realname,short,mid_id) VALUES ('%s','%s','%s')" % (realname[a_num], ab, mid)#写入短评表
            cursor.execute(sql2)#执行语句
            # short_new.append(ab)
            db.commit()#提交
            a_num = a_num + 1

        db.close()#关闭数据库





if __name__=='__main__':
#     # Douban_Crawl_data().text_01()
    Douban_Crawl_data().Douban_2()



