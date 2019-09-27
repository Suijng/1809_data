from django.db import models

# Create your models here.


# 学校表
class Schools(models.Model):
    name = models.CharField(max_length=56)  # 学校名
    url = models.CharField(max_length=256)  # 学校logo
    tese = models.CharField(max_length=56)  # 特色 211 985
    lishu = models.CharField(max_length=56)  # 隶属
    suozaidi = models.CharField(max_length=56)  # 所在地
    yuanshi = models.CharField(max_length=56)  # 院士
    boshi = models.CharField(max_length=56)  # 博士
    shuoshi = models.CharField(max_length=56)  # 硕士
    address = models.CharField(max_length=126)  # 地址
    phone = models.CharField(max_length=20)  # 电话
    email = models.CharField(max_length=30)  # 邮箱
    wangzhi = models.CharField(max_length=256)  # 网址
    jianjie = models.TextField() # 简介

    xingzhi = models.CharField(max_length=30)  # 性质 本科
    leixing = models.CharField(max_length=20) # 类型 综合 工本





