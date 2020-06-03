from django.db import models

# Create your models here.
# python3 manage.py makemigrations input #数据库迁移
# python3 manage.py migrate  # 同步数据库

# 电影id基础表
class Movie_base(models.Model):
    dou_name = models.CharField(max_length=1000)#豆瓣电影名字
    dou_id = models.CharField(max_length=1000)  # 豆瓣id

# 电影表
class Movie_list(models.Model):
    name = models.CharField(max_length=1000)#电影名字
    rating_num = models.CharField(max_length=1000)#评分数字

    def __str__(self):
        return self.name

# 短评表
class Content(models.Model):
    mid = models.ForeignKey(Movie_list,on_delete=models.CASCADE)  # 关联电影名字 id
    realname =  models.CharField(max_length=640) # 姓名
    short = models.CharField(max_length=10000)# 电影短评
    mid_name = models.CharField(max_length=1000)# 关联电影名字




    def __str__(self):
        return self.realname

# 明细表
class Detailed(models.Model):
    type = models.CharField(max_length=16) # 类型 1 收入 2 支出
    store = models.CharField(max_length=64) # 门店
    price = models.CharField(max_length=16) # 金额
    remark =  models.CharField(max_length=64)  # 备注
    create_time =  models.DateTimeField(auto_now=True)  # 创建时间
    other =  models.CharField(max_length=64)  # 其他


    def __str__(self):
        return self.remark

# 数据表


# 模仿祖冲之数据平台
# 用户表
# 消费表

# class wen_user(models.Model):
#     pass


class wen_order_record(models.Model):
    '''
    消费表
    '''
    name = models.CharField(max_length=64) # 名称
    mobile = models.CharField(max_length=16) # 手机号码
    order_amount = models.CharField(max_length=16) # 订单金额 单位：元
    status = models.CharField(max_length=16)#'订单状态  0：待支付  1：已支付  2：取消支付 3：支付失败',
    remark =  models.CharField(max_length=64)  # 备注
    pay_time =  models.DateField ()  # 消费时间,日期型，必须是“YYYY-MM-DD”格式
    create_time =  models.DateTimeField(auto_now=True)  # 创建时间


    def __str__(self):
        return self.remark

