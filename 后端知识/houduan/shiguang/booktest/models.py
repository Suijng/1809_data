from django.db import models

# Create your models here.

class daohang(models.Model):
    dtitle=models.CharField(max_length=20)

    def __str__(self):
        return self.dtitle

class mingpian(models.Model):
    mwangm=models.CharField(max_length=100)

    def __str__(self):
        return self.mwangm

class lei(models.Model):
    lname=models.CharField(max_length=20)

    def __str__(self):
        return self.lname

class wenzhang(models.Model):
    wtitle=models.CharField(max_length=50)
    wneirong=models.CharField(max_length=300)
    wdate=models.DateField()
    wpinglun=models.IntegerField(default=0)
    wdianzan=models.IntegerField(default=0)
    wimage=models.ImageField(upload_to='booktest/')
    wenlei=models.ForeignKey(lei)

    def __str__(self):
        return self.wtitle


#上传图片
class tupian(models.Model):
    tname=models.CharField(max_length=20)
    timage=models.ImageField(upload_to='booktest/')
    url=models.CharField(max_length=512)

    def __str__(self):
        return self.tname














