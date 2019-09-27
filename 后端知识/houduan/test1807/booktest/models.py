from django.db import models

# Create your models here.

'''
table_name booktest_bookinfo
先分析表结构
'''

class BookInfo(models.Model):
    btitle = models.CharField(max_length=20)
    bpub_date = models.DateField()

    def __str__(self):
        return self.btitle

#一对多 先分析表
class HeroInfo(models.Model):
    hname=models.CharField(max_length=20)
    hgender=models.BooleanField(default=True)
    hcontent=models.CharField(max_length=200)
    hbook=models.ForeignKey(BookInfo)#引用一对多的关系  必须写在多的里

    def __str__(self):
        return self.hname