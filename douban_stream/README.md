# 影评爬虫页面

### Bootcss + Django + Python 



# 安装依赖文件

` 安装依赖文件`

* pip install Django
* pip install pymysql
* pip install selenium
* 

# 同步数据库

` 使用的是mysql数据库，自行安装，快速搭建可以使用XAMPP,默认的账号是root密码空`

` 然后新建一个数据库，再执行下面操作`

* python manage.py migrate 同步表结构

* python manage.py createsuperuser 新增一个后台账号


# 本地运行

` 在文件根目录，运行命令，访问 http://127.0.0.1:8000/admin_0/`

* python manage.py runserver





























