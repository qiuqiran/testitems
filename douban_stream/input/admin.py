from django.contrib import admin
# from Slm.stream.input.models import Movie_list,Content
from input.models import Movie_list,Content,Detailed

# Register your models here.

class Movie_listadmin(admin.ModelAdmin):
    list_display = ['name','rating_num']
    search_fields = ['name'] #搜索栏
    # list_filter = ['']

class Contentadmin(admin.ModelAdmin):
    list_display = ['realname','short','mid']
    search_fields = ['realname'] #搜索栏
    list_filter = ['mid'] #过滤器

class Detailedadmin(admin.ModelAdmin):
    list_display = ['type','store','price','remark','create_time','other']
    search_fields = ['store'] #搜索栏
    # list_filter = ['']

admin.site.register(Movie_list,Movie_listadmin)
admin.site.register(Content,Contentadmin)
admin.site.register(Detailed,Detailedadmin)