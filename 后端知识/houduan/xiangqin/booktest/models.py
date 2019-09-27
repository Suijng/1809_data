from django.db import models

# Create your models here.

class User(models.Model):
    account=models.CharField(max_length=20,unique=True)
    password=models.CharField(max_length=256)
    nickname=models.CharField(max_length=20)
    gender=models.BooleanField(default=True)
    head=models.ImageField(upload_to='booktest/')
    isDelete=models.BooleanField(default=False)
    create_time=models.DateTimeField(auto_now_add=True)
    update_time=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.account
