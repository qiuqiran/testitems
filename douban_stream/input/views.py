from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from input.models import Movie_list,Content,Detailed
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# from urllib import request
import requests
import re
from bs4 import BeautifulSoup
import datetime



# Create your views here.

#首页管理
def index(request):
    Movies = Movie_list.objects.order_by('-id')#倒序输出所有电影列表
    shorts = Content.objects.order_by('-id')
    paginator = Paginator(shorts, 8)  # 每页展示数据数量
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        contacts = paginator.page(1)
    except EmptyPage:
        contacts = paginator.page(Paginator.num_pages)

    return render(request, 'index.html', {'Movie':Movies,'shorts':contacts})

#登录动作
def login_action(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)#登录
            request.session['user'] = username # 将 session 信息记录到浏览器
            resp = HttpResponseRedirect('/film/')#HttpResponseRedirect，它可以对路径进行重定向
            return resp
        else:
            return render(request,'admin_0.html', {'error': '不是账号错了就是密码错了!'})
    else:
        return render(request, 'admin_0.html', {'error': '不是账号错了就是密码错了!'})

#退出
def logout(request):
    auth.logout(request)
    resp = HttpResponseRedirect('/admin_0/')
    return resp


#电影列表管理
def list_manage(request):
    list = Movie_list.objects.order_by('-id')#倒序输出所有电影列表
    paginator = Paginator(list, 8)  # 每页展示数据数量
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        contacts = paginator.page(1)
    except EmptyPage:
        contacts = paginator.page(Paginator.num_pages)
    return render(request,'list_page.html',{'lists':contacts})

#短评列表管理
def content_manage(request,d):
    # username = request.session.get('user','')
    list =  Content.objects.filter(mid=str(d))#筛选对应的mid，使用d变量
    # list =  Content.objects.all()
    paginator = Paginator(list,8)#每页展示数据数量
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        contacts = paginator.page(1)
    except EmptyPage:
        contacts = paginator.page(Paginator.num_pages)
    return render(request,'content_page.html',{'lists':contacts})



#最新电影管理
def crawl_manage(request):
    from input.dcrawl.crawl import Douban_Nowplaying_link_num
    Douban_Nowplaying_link_num = Douban_Nowplaying_link_num()
    paginator = Paginator(Douban_Nowplaying_link_num, 8)  # 每页展示数据数量
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        contacts = paginator.page(1)
    except EmptyPage:
        contacts = paginator.page(Paginator.num_pages)
    return render(request,'crawl.html',{'link_num_lists':contacts})

#简介页面
def crawl_action(request,douban_id):
    from input.dcrawl.crawl import Douban_name
    Douban_name = Douban_name(douban_id)#页面获取douban_id，传到crawl.py做爬取
    return render(request,'reptilian_de.html',{'lists':Douban_name})






#测试入口
def newspaper(request,k):
    # Movies = Movie_list.objects.order_by('mid_id')  # 倒序输出所有电影列表
    shorts = Content.objects.filter(mid=str(k))
    return render(request, 'newspaper.html', {'shorts': shorts})



#报错入口
def page_not_found(request):
    return render(request,'404.html')

def page_error(request):
    return render(request,'500.html')


#新首页
def new_index(request):
    url = 'https://api.seniverse.com/v3/weather/now.json?'
    data = {'key': 'a5ecl6fjnuuoeoy1', 'location': 'shenzhen', 'language': 'zh-Hans', 'unit': 'c'}
    link = requests.get(url, data)
    difan = link.json()['results'][0]['location']['name']
    tianqi = link.json()['results'][0]['now']['text']
    dushu = link.json()['results'][0]['now']['temperature']
    riqi = link.json()['results'][0]['last_update'][0:10]
    num = len(Movie_list.objects.all())

    short_list =  Content.objects.order_by('-id')
    paginator = Paginator(short_list, 8)  # 每页展示数据数量
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        contacts = paginator.page(1)
    except EmptyPage:
        contacts = paginator.page(Paginator.num_pages)



    #----------------3条短评
    # from input.dcrawl.crawl import new_index_crawl_realname
    # from input.dcrawl.crawl import new_index_crawl_short
    # new_index_crawl_realname= new_index_crawl_realname()
    # new_index_crawl_short=new_index_crawl_short()
    #
    # #-----------------3条电影
    # from input.dcrawl.crawl import new_index_crawl_movie
    # new_index_crawl_movie=new_index_crawl_movie()
    #
    # #-----------------img
    # from input.dcrawl.crawl import new_index_crawl_img
    # new_index_crawl_img=new_index_crawl_img()
    #
    # #-----------------rating_num
    # from input.dcrawl.crawl import new_index_crawl_rating_num
    # new_index_crawl_rating_num=new_index_crawl_rating_num()
    #
    # #----------------
    # from input.dcrawl.crawl import new_index_crawl_week_top
    # new_index_crawl_week_top=new_index_crawl_week_top()
    #
    #
    #
    # #-------------------
    # from input.dcrawl.crawl import new_index_crawl_na_top
    # new_index_crawl_na_top=new_index_crawl_na_top()


    return render(request, 'new_index.html', {'short_list':contacts})
# 'tianqi': tianqi, 'difan': difan, 'dushu': dushu, 'riqi': riqi, 'num': num,
#                                               'realname':new_index_crawl_realname,'short':new_index_crawl_short,
#                                               'name':new_index_crawl_movie,'img':new_index_crawl_img,
#                                               'rating_num':new_index_crawl_rating_num,
#                                               'week_top':new_index_crawl_week_top,
#                                               'na_top':new_index_crawl_na_top,


#album
def album(request):

    return render(request,'album.html')

def admin_0(request):
    return render(request,'admin_0.html')






@login_required()
def api_page(request):
    return render(request,'api_page.html')

@login_required()
def comment(request,id):
    '''后台短评列表'''
    list = Content.objects.filter(mid=id)
    paginator = Paginator(list, 10)  # 每页展示数据数量
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        contacts = paginator.page(1)
    except EmptyPage:
        contacts = paginator.page(Paginator.num_pages)
    return render(request, 'comment.html', {'lists': contacts})

def cover(request):

    # movie_mid = Movie_list.objects.order_by('?')#随机获取电影mid_id
    list = Content.objects.filter(mid=16)#在获取第一个电影里面的短评
    # list = Content.objects.order_by('?')#随机一条短评



    return render(request,'cover.html', {'lists': list})

def cover2(request,):

    movie = Movie_list.objects.order_by('-id')
    # paginator = Paginator(movie, 10)  # 每页展示数据数量
    # page = request.GET.get('page')
    # try:
    #     contacts = paginator.page(page)
    # except PageNotAnInteger:
    #     contacts = paginator.page(1)
    # except EmptyPage:
    #     contacts = paginator.page(Paginator.num_pages)


    return render(request,'cover2.html', {'lists': movie})


@login_required()
def film(request):
    '''后台电影列表'''
    movie = Movie_list.objects.order_by('-id')
    paginator = Paginator(movie, 10)  # 每页展示数据数量
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        contacts = paginator.page(1)
    except EmptyPage:
        contacts = paginator.page(Paginator.num_pages)

    return render(request,'film.html',{'lists':contacts})



# 早餐车项目

def breakfast(request):
    return render(request,'breakfast.html')

def breakfast_login(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)  # 登录
            request.session['user'] = username  # 将 session 信息记录到浏览器
            resp = HttpResponseRedirect('/breakfast1/')  # HttpResponseRedirect，它可以对路径进行重定向
            return resp
        else:
            return render(request, 'breakfast.html', {'error': '不是账号错了就是密码错了!'})
    else:
        return render(request, 'breakfast.html', {'error': '不是账号错了就是密码错了!'})


def breakfast_logout(request):
    auth.logout(request)
    resp = HttpResponseRedirect('/breakfast/')
    return resp
@login_required()
def breakfast1(request):
    '''统计页面'''
    detailed = Detailed.objects.order_by('-id')
    detailed_in = Detailed.objects.filter(type='收入').order_by('-id')
    detailed_out = Detailed.objects.filter(type='支出').order_by('-id')

    paginator = Paginator(detailed, 10)  # 每页展示数据数量
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        contacts = paginator.page(1)
    except EmptyPage:
        contacts = paginator.page(Paginator.num_pages)

    return render(request, 'breakfast1.html', {'lists': contacts,'detailed_in':detailed_in,'detailed_out':detailed_out})
@login_required()
def breakfast2(request):
    '''新增页面'''
    return render(request,'breakfast2.html')
@login_required()
def breakfast_create(request):
    type = request.POST.get('type','类型')
    store = request.POST.get('store','岗厦C')
    price = request.POST.get('price','696')
    remark = request.POST.get('remark','默认标题')
    other = request.POST.get('other','默认备注')

    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    xie = Detailed(type=type,store=store,price=price,remark=remark,create_time=now,other=other)
    xie.save()
    resp = HttpResponseRedirect('/breakfast1/')
    return resp

def grid(request):
    '''
    grid 网格页面，2019-8-1
    :param request:
    :return:
    '''
    return render(request,'grid.html')

def astrology(request):
    """

    :param request:
    :return:
    """
    return render(request,'astrology.html')



def o4(request):

    return render(request,'o4.html')

def argon_index(request):
    return render(request,'argon_index.html')

def argon_login(request):
    '''
    登录页面
    :param request:
    :return:
    '''
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)  # 登录
            request.session['user'] = username  # 将 session 信息记录到浏览器
            resp = HttpResponseRedirect('/dashboard/')  # HttpResponseRedirect，它可以对路径进行重定向
            return resp
        else:
            return render(request, 'argon_index.html', {'error': '登录错误!'})
    else:
        return render(request, 'argon_index.html', {'error': '登录失败!'})


def argon_logout(request):
    '''
    退出
    :param request:
    :return:
    '''
    auth.logout(request)
    resp = HttpResponseRedirect('/argon_index/')
    return resp

def dashboard(request):
    '''

    :param request:
    :return:
    '''
    return render(request,'dashboard.html')


def tables(request):
    '''

    :param request:
    :return:
    '''
    list = Movie_list.objects.order_by('-id')  # 倒序输出所有电影列表
    paginator = Paginator(list, 5)  # 每页展示数据数量
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        contacts = paginator.page(1)
    except EmptyPage:
        contacts = paginator.page(Paginator.num_pages)
    return render(request, 'tables.html', {'lists': contacts})


def tables_de(request,d):
    '''

    :param request:
    :return:
    '''
    # username = request.session.get('user','')
    list = Content.objects.filter(mid=str(d))  # 筛选对应的mid，使用d变量
    # list =  Content.objects.all()
    paginator = Paginator(list, 4)  # 每页展示数据数量
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        contacts = paginator.page(1)
    except EmptyPage:
        contacts = paginator.page(Paginator.num_pages)
    return render(request, 'tables_de.html', {'lists': contacts})

def reptilian_de(request):
    '''

    :param request:
    :return:
    '''
    return render(request, 'reptilian_de.html')


@login_required()
def reptilian(request):
    '''
    爬虫页面
    :param request:
    :return:
    '''
    from input.dcrawl.crawl import Douban_Nowplaying_lists
    return render(request, 'reptilian_de.html', {'lists': Douban_Nowplaying_lists})




def crawl_save(request,douban_id):
    '''
    拿到id，然后去爬取，然后写入数据库
    :param request:
    :param douban_id:
    :return:
    '''
    from input.dcrawl.crawl import Douban_crawl
    from input.dcrawl.crawl import Douban_Nowplaying_lists

    Douban_crawl(douban_id)

    return render(request, 'reptilian_de.html', {'lists': Douban_Nowplaying_lists})