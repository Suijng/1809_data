# post_save  Django中的model对象保存后,自动触发
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model

# 获取用户模型
User = get_user_model()

@receiver(post_save,sender=User) # 监控用户User模型
def create_user(sender,instance=None,created=False,**kwargs):
    # created: 表示是否已经创建
    if created:
        # 获取用户的密码
        password = instance.password
        # 加密
        instance.set_password(password)
        # 保存
        instance.save()