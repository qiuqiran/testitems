#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from urllib import request
import re
import MySQLdb
from bs4 import BeautifulSoup


class Douban_Nowplaying():
    '''豆瓣最新上映电影'''

    def tes_01(self):

        url = 'https://movie.douban.com/cinema/nowplaying/shenzhen/'
        html = request.urlopen(url).read().decode('utf-8')

        na = re.findall(r'alt="(.*?)" rel="nofollow"',html)
        link_num = re.findall(r'<a href="https://movie.douban.com/subject/(.*?)/\?from=playing_poster" class=ticket-btn target="_blank" data-psource="poster">',html)
        img ='ss'
        print(na)
        print(len(na))
        print(len(link_num))
        a = []
        b = 0
        while b <32:
            a.append(na[b])
            b = b + 1
        print(a)
        print(len(a))
        lists = dict(zip(a,link_num))
        print(lists)




    def test_02(self):

        url = 'https://movie.douban.com/subject/26336252/?from=showing'
        html = request.urlopen(url).read().decode('utf-8')

        soup = BeautifulSoup(html, 'html.parser')
        nam = soup.find_all('span', {'property': 'v:summary'})  # 短评,换一种方法就可以获取到
        name = re.findall(r'<span property="v:itemreviewed">(.*?)</span>',html)
        for i in nam:
            link_num = i.get_text().strip().replace("\n", "")
        a = {'name':name[0],'jianjie':link_num}
        # print(a)
        actor = soup.find_all('span', {'class': 'attrs'})
        aa = re.findall(r'<rel="v:starring">(.*?)</a>',html)

        # print(aa)
        # print(actor)

        img =re.findall(r'<img src="(.*?)" title="点击看更多海报"',html)
        print(img)
        starring = re.findall(r'rel="v:starring">(.*?)</a> /',html)
        print(starring)
        for i in starring:
            print(i)

    def tesss(self):
        a = range(len('sdsf'))
        for i in a:
            print(i)




if __name__=='__main__':
    # Douban_Nowplaying().tes_01()
    # Douban_Nowplaying().test_02()
    Douban_Nowplaying().tesss()