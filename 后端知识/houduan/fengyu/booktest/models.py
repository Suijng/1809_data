from django.db import models

# Create your models here.

#导航
class daohang(models.Model):
    dtitle=models.CharField(max_length=20)

    def __str__(self):
        return self.dtitle

#轮播图片
class lunbo(models.Model):
    lname=models.CharField(max_length=20)
    limage=models.ImageField(upload_to='booktest/')
    is_active = models.BooleanField(default=False)
    lurl=models.CharField(max_length=512)

    def __str__(self):
        return self.lname

#标签
class biaoqian(models.Model):
    btitle=models.CharField(max_length=100)

    def __str__(self):
        return self.btitle

#发布正文
class fabu(models.Model):
    ftitle=models.CharField(max_length=100)
    fneirong=models.CharField(max_length=500)
    fname=models.CharField(max_length=20)
    fyuedu=models.IntegerField(default=0)
    fpinglun=models.IntegerField(default=0)
    fdate=models.DateField()
    ftupian=models.ImageField(upload_to='booktest/')
    fbq=models.ManyToManyField(biaoqian)

    def __str__(self):
        return self.ftitle
