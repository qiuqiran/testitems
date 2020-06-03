from django.test import TestCase
from input.models import Movie_list,Content
from django.test import Client
#

# Create your tests here.
#运行方法是在 项目地址： python manage.py test
#运行其中一个class：python manage.py test input.tests.IndexPageTest
#运行class其中一个def：python manage.py test input.tests.IndexPageTest.test_index_page
#运行模糊匹配测试文件：python manage.py test -p test*.py

class ModelsTest(TestCase):
    '''modle单元测试'''
    def setUp(self):
        '''电影列表和评论列表新增一条数据
        Django 在执行 setUp()方法中的数据库初始化时，并非真正的向数据库表中插入了数据。所以，数据库并
        不会因为运行测试而产生测试数据。'''

        Movie_list.objects.create(id=1,name='Crazy Rich Asians',rating_num=7.6)
        Content.objects.create(realname='kew',short='content_test',mid_id=1)

    def test_movie_list_models(self):

        result = Movie_list.objects.get(name='Crazy Rich Asians')#找到setUp()初始化的数据
        self.assertAlmostEqual(str(result.rating_num),str(7.6))#断言插入的评分

    def test_content_models(self):
        result = Content.objects.get(realname='kew')
        self.assertAlmostEqual(result.short,'content_test')
        self.assertAlmostEqual(result.mid_id,1)


class IndexPageTest(TestCase):
    '''首页单元测试'''
    def test_index_page(self):
        '''index视图测试'''
        response = self.client.get('/')
        # self.assertAlmostEqual(response.status_code,200)
        self.assertEqual(response.status_code,200)#assertEqual()服务器对客户端的应答是否为 200
        self.assertTemplateUsed(response,'index.html')#assertTemplateUsed()断言是否用给定的是 index.html 模版响应。


class ListPageTest(TestCase):
    '''电影列表单元测试'''
    def setUp(self):
        Movie_list.objects.create(id=1,name='Crazy Rich Asians',rating_num=7.6)
        self.c = Client()
    def test_list_page(self):
        response = self.c.post('/list_page/')
        self.assertEqual(response.status_code,200)
        self.assertIn(b'Crazy Rich Asians',response.content)#判断a in b是否成立，
        self.assertIn(b'7.6',response.content)
        self.assertTemplateUsed(response,'list_page.html')


class TestPageTest(TestCase):
    '''测试入口单元测试'''
    def setUp(self):
        self.c = Client()
    def test_test_page(self):
        response = self.c.get('/test/')
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'newspaper.html')
        self.assertIn(b'mysql',response.content)
        self.assertIn(b'207.246.77.150',response.content)

class ContentPageTest(TestCase):
    '''短评列表单元测试'''
    def setUp(self):
        Movie_list.objects.create(id=1,name='Crazy Rich Asians',rating_num=7.6)
        Content.objects.create(realname='kew',short='content_test',mid_id=1)
        Content.objects.create(realname='wen',short='content_test2',mid_id=1)
        self.c = Client()
    def test_content_page(self):
        response = self.c.post('/content_page/1/')
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'content_page.html')
        self.assertIn(b'content_test',response.content)
        self.assertIn(b'wen',response.content)


