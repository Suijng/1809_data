from django.db import models
from datetime import datetime

# Create your models here.


# 用户表
class User(models.Model):
    USER_TYPE = (
        (1,'VIP'),
        (2,'普通用户')
    )
    USER_GENDER = (
        (1,'男'),
        (2,'女')
    )
    # 用户名
    name = models.CharField(max_length=128,null=False)
    # 用户类型 (普通类型,VIP类型)
    type = models.IntegerField(choices=USER_TYPE,default=2)
    # 密码
    password = models.CharField(max_length=15,null=False)
    # 性别
    gender = models.IntegerField(choices=USER_GENDER,default=1)
    # 出生日期
    birthday = models.DateTimeField(default=datetime.now)


# 登录token
class Token(models.Model):
    # 跟用户关联
    user = models.OneToOneField(User)
    # 用户登录成功后的token提示
    token = models.CharField(max_length=128)


# 商品分类
class Category(models.Model):
    categoryname = models.CharField(max_length=56)  # 分类名称


#  属性
class Attribute(models.Model):
    attr = models.CharField(max_length=30)  # 颜色或者尺寸
    jieshao = models.IntegerField(default=0) # 默认是颜色


# 商品列表
class Clothes(models.Model):
    yifuname = models.CharField(max_length=56)  # 衣服名字
    yifuprice = models.FloatField()  # 价格
    yifunum = models.CharField(max_length=10)  # 数量
    yifuurl = models.CharField(max_length=256) # 图片地址
    category = models.ForeignKey(Category)  # 一对多 所在的哪类衣服


#  中间表
class ClothesAttr(models.Model):
    size = models.ForeignKey(Attribute,related_name='size',null=False,blank=True)  # 对应的尺寸
    color = models.ForeignKey(Attribute,related_name='color',null=False,blank=True)  # 对应的颜色
    good = models.ForeignKey(Clothes) # 商品外键


# 购物车
class Shopcar(models.Model):
    carname = models.CharField(max_length=56)  # 衣服名字
    carsize = models.CharField(max_length=10)  # 尺码
    carnum = models.CharField(max_length=10)  # 数量
    carurl = models.CharField(max_length=256)  # 图片地址
    carxuan = models.IntegerField(default=0) # 默认没选中
    carprice = models.FloatField()  # 价格
    user = models.ForeignKey(User)  # 哪个用户的购物车


#  地址
class Address(models.Model):
    dizhiname = models.CharField(max_length=256)  # 地址
    dizhimoren = models.IntegerField(default=0)  # 0是默认地址
    user = models.ForeignKey(User)  # 哪个用户的地址




