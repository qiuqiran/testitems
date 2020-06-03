#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from urllib import request
import re
from bs4 import BeautifulSoup
from input.models import Movie_list,Content


def Douban_Nowplaying_name():
    '''最新上架电影名字和id'''
    url = 'https://movie.douban.com/cinema/nowplaying/shenzhen/'
    html = request.urlopen(url).read().decode('utf-8')
    na = re.findall(r'alt="(.*?)" rel="nofollow"', html)
    return na



def Douban_Nowplaying_link_num():
    '''最新上架电影id'''
    url = 'https://movie.douban.com/cinema/nowplaying/shenzhen/'
    html = request.urlopen(url).read().decode('utf-8')
    link_num = re.findall(r'<a href="https://movie.douban.com/subject/(.*?)/\?from=playing_poster" class=ticket-btn target="_blank" data-psource="poster">',html)
    return link_num


def Douban_name(douban_id):
    '''
    豆瓣单部电影简介
    :param douban_id:
    :return:
    '''
    douban_id = douban_id  # 豆瓣id，由页面传过来
    surl = 'https://movie.douban.com/subject/' + douban_id + '/?from=showing'  # 首页
    # url = 'https://movie.douban.com/subject/26336252/?from=showing'
    html = request.urlopen(surl).read().decode('utf-8')

    soup = BeautifulSoup(html, 'html.parser')
    nam = soup.find_all('span', {'property': 'v:summary'})  # 短评,换一种方法就可以获取到
    name = re.findall(r'<span property="v:itemreviewed">(.*?)</span>', html)
    img = re.findall(r'<img src="(.*?)" title="点击看更多海报"', html)
    starring = re.findall(r'rel="v:starring">(.*?)</a> /', html)

    for i in nam:
        link_num = i.get_text().strip().replace("\n", "")
    actor = soup.find_all('span', {'class': 'actor'})
    for k in actor:
        actor1 = k.get_text().strip().replace("\n", "")
    a = {'name': name[0], 'jianjie': link_num,'doubanid':douban_id,'actor1':actor1[0],'img':img[0],'starring1':starring[0],'starring2':starring[1],'starring3':starring[3], 'starring4': starring[4],'starring5':starring[5],'starring6':starring[6]}
    return a

def Douban_crawl(douban_id):
    '''
    拿到id，去插入数据库
    :param douban_id:
    :return:
    '''

    douban_id = douban_id  # 豆瓣id
    page_num = str(20 * 1)  # 页数

    surl = 'https://movie.douban.com/subject/' + douban_id + '/'  # 首页
    shtml = request.urlopen(surl).read().decode('utf-8')
    name = re.findall(r'<span property="v:itemreviewed">(.*?)</span>', shtml)  # 获取标题
    rating_num = re.findall(r'<strong class="ll rating_num" property="v:average">(.*?)</strong>', shtml)  # 获取点评分数


    sql = Movie_list.objects.all()
    id = len(sql) + 1

    sql1 = Movie_list(id=id,name=name[0],rating_num=rating_num[0])
    sql1.save()

    url = 'https://movie.douban.com/subject/' + douban_id + '/comments?start=' + page_num + '&limit=20&sort=new_score&status=P'  # 短评页
    html = request.urlopen(url).read().decode('utf-8')
    realname = re.findall(r'<a.+people.+">(.+)</a>', html)  # 用户名
    soup = BeautifulSoup(html, 'html.parser')
    short = soup.find_all('span', {'class': 'short'})  # 短评,换一种方法就可以获取到
    mid = id
    a_num = 0
    while a_num < 20:
        ab = short[a_num].get_text().strip().replace("\n", "")  # 取代html标签，并且去掉豆瓣第一条短评空格换行
        try:#有些有表情无法插入数据库，报错就跳过
            sql2 = Content(realname=realname[a_num],short=ab,mid_id=mid)
            sql2.save()
            a_num = a_num + 1
        except:
            a_num = a_num + 1


def new_index_crawl_realname():
    '''
    由首页拿取最新的电影id，然后去查看这个部电影的最新3条用户名
    :return:
    '''
    url = 'https://movie.douban.com/cinema/nowplaying/shenzhen/'
    html = request.urlopen(url).read().decode('utf-8')
    link_num = re.findall(r'<a href="https://movie.douban.com/subject/(.*?)/\?from=playing_poster" class=ticket-btn target="_blank" data-psource="poster">',html)

    douban_id = link_num[0]  # 豆瓣id
    page_num = str(20 * 0)  # 页数

    url = 'https://movie.douban.com/subject/' + douban_id + '/comments?start=' + page_num + '&limit=20&sort=new_score&status=P'  # 短评页
    html = request.urlopen(url).read().decode('utf-8')
    realname = re.findall(r'<a.+people.+">(.+)</a>', html)  # 用户名
    a = {'realname1':realname[0],'realname2':realname[1],'realname3':realname[2]}
    return a


def new_index_crawl_short():
    '''
    由首页拿取最新的电影id，然后去查看这个部电影的最新3条短评
    :return:
    '''
    url = 'https://movie.douban.com/cinema/nowplaying/shenzhen/'
    html = request.urlopen(url).read().decode('utf-8')
    link_num = re.findall(
        r'<a href="https://movie.douban.com/subject/(.*?)/\?from=playing_poster" class=ticket-btn target="_blank" data-psource="poster">',
        html)

    douban_id = link_num[0]  # 豆瓣id
    page_num = str(20 * 0)  # 页数

    url = 'https://movie.douban.com/subject/' + douban_id + '/comments?start=' + page_num + '&limit=20&sort=new_score&status=P'  # 短评页
    html = request.urlopen(url).read().decode('utf-8')
    soup = BeautifulSoup(html, 'html.parser')
    short = soup.find_all('span', {'class': 'short'})  # 短评,换一种方法就可以获取到
    ab1 = short[0].get_text().strip().replace("\n", "")
    ab2 = short[1].get_text().strip().replace("\n", "")
    ab3= short[2].get_text().strip().replace("\n", "")
    b = {'short1':ab1,'short2':ab2,'short3':ab3}
    return b


def new_index_crawl_img():
    '''
    图片
    :return:
    '''
    url = 'https://movie.douban.com/cinema/nowplaying/shenzhen/'
    html = request.urlopen(url).read().decode('utf-8')
    img = re.findall(r'<img src="(.*?)"', html)
    return img

def new_index_crawl_rating_num():
    '''
    评分
    :return:
    '''
    url = 'https://movie.douban.com/cinema/nowplaying/shenzhen/'
    html = request.urlopen(url).read().decode('utf-8')
    rating_num = re.findall(r'<span class="subject-rate">(.*?)</span>',html)
    return rating_num

def new_index_crawl_week_top():
    '''
    一周口碑榜
    :return:
    '''
    url = 'https://movie.douban.com/chart'
    html = request.urlopen(url).read().decode('utf-8')
    soup = BeautifulSoup(html, 'html.parser')
    name = soup.find_all('div', {'class': 'name'})
    k = []
    for i in name:
        ab = i.get_text().strip().replace("\n", "")
        k.append(ab)
    return k


def new_index_crawl_na_top():
    '''
    北美票房榜
    :return:
    '''

    url = 'https://movie.douban.com/chart'
    html = request.urlopen(url).read().decode('utf-8')
    soup = BeautifulSoup(html, 'html.parser')
    name = soup.find_all('div', {'class': 'box_chart'})
    l = []
    for i in name:
        ab = i.get_text().strip().replace("\n", "")
        l.append(ab)
    return l

def Douban_Nowplaying_lists():
    '''
    最新的电影列表，包含id和名字
    :return:
    '''
    name = Douban_Nowplaying_name()
    id = Douban_Nowplaying_link_num()
    # rating = new_index_crawl_rating_num()
    # print(name,id,rating)
    l = []
    for i in range(len(id)):
        # print(name[i],id[i])
        l.append({'name':name[i],'id':id[i]})
    return l[0:6]
