from django.db import models

# Create your models here.

#分类
class Category(models.Model):
    types = models.CharField(max_length=20)

    is_delete=models.BooleanField(default=False)#是否删除
    create_time=models.DateTimeField(auto_now_add=True)#创建时间
    update_time=models.DateTimeField(auto_now=True)#更新时间

    def __str__(self):
        return self.types


#小说
class Article(models.Model):
    title = models.CharField(max_length=20)
    content = models.CharField(max_length=3000)
    wenfenlei = models.ForeignKey(Category)
    is_delete=models.BooleanField(default=False)#是否删除
    create_time=models.DateTimeField(auto_now_add=True)#创建时间
    update_time=models.DateTimeField(auto_now=True)#更新时间

    def __str__(self):
        return self.title


#章节
class zhangJe(models.Model):
    title = models.CharField(max_length=40)
    name = models.CharField(max_length=40)
    xiaozhai = models.ForeignKey(Article)
    is_delete=models.BooleanField(default=False)#是否删除
    create_time=models.DateTimeField(auto_now_add=True)#创建时间
    update_time=models.DateTimeField(auto_now=True)#更新时间

    def __str__(self):
        return self.name





