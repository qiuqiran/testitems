"""stream URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from input import views


# from Slm.stream.input.views import list_manage

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.argon_index),
    url(r'^reptilian/login_action/$', views.login_action),
    url(r'^content_page/(\d+)/$',views.content_manage,name='content_manage'),#name=指向views里面

    url(r'^crawl/$',views.crawl_manage),
    url(r'^crawl_action/(\d+)/$',views.crawl_action),

    url(r'^newspaper/$',views.newspaper),
    url(r'^newspaper/(\d+)/$', views.newspaper,name='newspaper'),
    url(r'^breakfast/$', views.breakfast),
    url(r'^breakfast_login/$', views.breakfast_login),
    url(r'^breakfast1/$', views.breakfast1),
    url(r'^breakfast2/$', views.breakfast2),
    url(r'^breakfast_logout/$', views.breakfast_logout),
    url(r'^breakfast_create/$', views.breakfast_create),
    # url(r'^breakfast_create/(?P<id>[0-9]+)/$', views.breakfast_create),

    url(r'^new_index/$',views.new_index),
    url(r'^album/$',views.album),
    url(r'^admin_0/$', views.admin_0),
    url(r'^reptilian/$',views.reptilian),
    url(r'^api_page/$',views.api_page),
    url(r'^comment/(\d+)/$', views.comment),

    url(r'^api/',include('input.urls',)),#配置具体接口的二级路径。
    url(r'^logout/$',views.logout),
    url(r'^cover/$', views.cover),
    url(r'^grid/$',views.grid),# 2019/8/1 新页面，其他抛掉
    url(r'^film/$',views.film),
    url(r'^cover2/$', views.cover2),



    url(r'^argon_index/$', views.argon_index),# 首页
    url(r'^argon_login/$', views.argon_login),  # 登录动作
    url(r'^argon_logout/$', views.argon_logout),  # 退出动作

    url(r'^dashboard/$', views.dashboard), # 登录后跳转页面
    url(r'^tables/$', views.tables),  # 电影列表页面
    url(r'^tables_de/(\d+)/$', views.tables_de, name='tables_de'),  # name=指向views里面
    url(r'^reptilian_de/$', views.reptilian), # 爬虫页面
    url(r'^crawl_save/(\d+)/$', views.crawl_save),
    url(r'^astrology/$', views.astrology),

]

handler404 = views.page_not_found
handler500 = views.page_error