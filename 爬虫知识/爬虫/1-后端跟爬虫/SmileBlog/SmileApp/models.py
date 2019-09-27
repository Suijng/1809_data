from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=50)#标题
    content = RichTextUploadingField()#内容
    read_num = models.IntegerField(default=0)#阅读数
    top = models.BooleanField(default=False)#推荐
    isDelete = models.BooleanField(default=False)#是否被删除
    position = models.IntegerField(default=0, null=True)#定位
    create_time = models.DateTimeField(auto_now_add=True, null=True)
    update_time = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '文章标题'
        verbose_name_plural = verbose_name


class Photo(models.Model):
    title = models.CharField(max_length=50)#标题
    img = models.ImageField(upload_to='smile/')#图片
    read_num = models.IntegerField(default=0)#阅读数
    top = models.BooleanField(default=False)#推荐
    isDelete = models.BooleanField(default=False)#是否被删除
    position = models.IntegerField(default=0, null=True)
    create_time = models.DateTimeField(auto_now_add=True, null=True)
    update_time = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '图片标题'
        verbose_name_plural = verbose_name
