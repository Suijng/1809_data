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
    type = models.IntegerField(choices=USER_TYPE,default=0)
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


# 书籍分类
class Category(models.Model):
    categoryname = models.CharField(max_length=56) # 分类名称
    info = models.CharField(max_length=256) # 分类介绍
    add_time = models.DateTimeField(default=datetime.now) # 添加时间


# 书籍
class Book(models.Model):
    BOOK_STATE = (
        (1, '完结'),
        (2, '连载中')
    )
    bookname = models.CharField(max_length=56)  # 书名
    bookjie = models.CharField(max_length=256)  #  书籍介绍
    bauthor = models.CharField(max_length=56)  # 作者
    bstate = models.IntegerField(choices=BOOK_STATE,default=1)  # 状态(完结,连载)
    category = models.ForeignKey(Category)  # 所属书籍分类
    burl = models.CharField(max_length=256)  # 封面图片的地址
    add_time = models.DateTimeField(default=datetime.now)  # 添加时间


# 章节
class Chpater(models.Model):
    CHAPTER_VIP = (
        (1, 'VIP'),
        (2, '普通用户')
    )
    chpatername = models.CharField(max_length=56)  # 章节名称
    chcontent = models.TextField  # 章节内容
    book = models.ForeignKey(Book)  # 所属书籍
    add_time = models.DateTimeField(default=datetime.now)  # 添加时间
    chvip = models.BooleanField(default=False)  # 默认普通用户








