from django.db import models
from tinymce.models import HTMLField

from  ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.


class BookInfo(models.Model):
    btitle = models.CharField(max_length=20)#图书名称
    bpub_date = models.DateField()#发布日期
    bread = models.IntegerField(default=0)#阅读量
    bcomment = models.IntegerField(default=0)#评论量
    isDelete = models.BooleanField(default=False)#逻辑删除

    def show(self):
        return '老王'

    def __str__(self):
        return self.btitle


    #元选项
    class Meta:
        ordering = ['-bpub_date']#排序
        verbose_name='书籍'  #单数
        verbose_name_plural=verbose_name #复数


class HeroInfo(models.Model):
    hname = models.CharField(max_length=20)#英雄姓名
    hgender = models.BooleanField(default=True)#英雄性别
    isDelete = models.BooleanField(default=False)#逻辑删除
    hcomment = models.CharField(max_length=200)#英雄描述信息
    hbook = models.ForeignKey('BookInfo')

    def __str__(self):
        return self.hname

    def gender(self):
        if self.hgender:
            return '男'
        else:
            return '女'
    def name(self):
        return self.hname

    #让函数根据hgender排序
    gender.admin_order_field='hgender'

    gender.short_description='性别'

    name.short_description='姓名'

class TestPic(models.Model):
    timage=models.ImageField(upload_to='booktest/')

class AreaInfo(models.Model):
    atitle=models.CharField(max_length=20)
    aParent=models.ForeignKey('self',null=True,blank=True)

    def __str__(self):
        return self.atitle

class goodsinfo(models.Model):
    gcontent=HTMLField()

class Article(models.Model):
    title = models.CharField(max_length=20)
    content = RichTextUploadingField()


