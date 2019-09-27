from django.db import models

# Create your models here.

from datetime import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser


# 用户
class UserProfile(AbstractUser):
    GENDER_TYPE = (
        ("male", "男"),
        ("female", "女")
    )
    name = models.CharField(max_length=32, null=True, blank=True, verbose_name="姓名")
    birthday = models.DateField(default=datetime.now,verbose_name="出生年月")
    gender = models.CharField(choices=GENDER_TYPE, max_length=20,default="male", verbose_name="性别")
    mobile = models.CharField(max_length=11, null=True, blank=True, verbose_name="电话")
    email = models.EmailField(max_length=256, null=True, blank=True, verbose_name="邮箱")

    class Meta:
        verbose_name = "用户"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


#  短信验证码
class VerifyCode(models.Model):
  code = models.CharField(max_length=6, null=False,verbose_name="验证码")  # 验证码
  mobile = models.CharField(max_length=11, null=False,verbose_name="电话")  # 手机号
  add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")  # 添加时间

  class Meta:
    verbose_name = "短信验证码"
    verbose_name_plural = verbose_name

  def __str__(self):
    return self.code