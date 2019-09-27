from django.db import models
from datetime import datetime
# Create your models here.
#真.自定义管理器
class BookInfoManger(models.Manager):

    def all(self):
        queryset=super().all()
        #做点逻辑
        queryset.reverse()
        return queryset

    def create(self,title):
        b=BookInfo()
        b.btitle=title
        b.bpub_date=datetime.now()
        b.save()





class BookInfo(models.Model):
    btitle = models.CharField(max_length=20)#图书名称
    bpub_date = models.DateField()#发布日期
    bread = models.IntegerField(default=0)#阅读量
    bcomment = models.IntegerField(default=0)#评论量
    isDelete = models.BooleanField(default=False)#逻辑删除

    def __str__(self):
        return self.btitle


    #自定义管理器 这个管理器只是换了个名字
    o=models.Manager()
    # 自定义管理器
    book2=BookInfoManger()


class HeroInfo(models.Model):
    hname = models.CharField(max_length=20)#英雄姓名
    hgender = models.BooleanField(default=True)#英雄性别
    isDelete = models.BooleanField(default=False)#逻辑删除
    hcomment = models.CharField(max_length=200)#英雄描述信息
    hbook = models.ForeignKey('BookInfo')

    def __str__(self):
        return self.hname




class AreaInfo(models.Model):
    atitle=models.CharField(max_length=20)
    aParent=models.ForeignKey('self',null=True,blank=True)

    def __str__(self):
        return self.atitle
