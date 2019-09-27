from django.db import models

# Create your models here.

class Shouye(models.Model):
    stitle=models.CharField(max_length=20,db_column='naeme')

    def __str__(self):
        return self.stitle


class Xiangxi(models.Model):
    xtitle=models.CharField(max_length=100)
    xname=models.CharField(max_length=20)
    shijie=models.CharField(max_length=20)
    xdate=models.DateTimeField()

    def  __str__(self):
        return self.xtitle

