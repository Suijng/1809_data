from django.db import models

# Create your models here.


class Mingzhan(models.Model):
    mtitle=models.CharField(max_length=20)
    index = models.IntegerField()

    def __str__(self):
        self.mtitle


class Baidu(models.Model):
    bname=models.CharField(max_length=20)
    address=models.CharField(max_length=512)
    index=models.IntegerField()
    topnav=models.ForeignKey(Mingzhan)

    def __str__(self):
        self.bname
