from django.db import models
from datetime import datetime

# Create your models here.

# 用户名 用户类型(普通用户 VIP用户) 密码 性别 出生日期

class User(models.Model):
    USER_TYPE = (
        (1,'VIP'),
        (0,'普通用户')
    )
    USER_GENDER = (
        (1,'男'),
        (0,'女')
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


class Token(models.Model):
    # 跟用户关联
    user = models.ForeignKey(User)
    # 用户登录成功后的token提示
    token = models.CharField(max_length=128)

