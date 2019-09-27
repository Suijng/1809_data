from django.db import models
from userapp.models import BlogUser

from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.

#轮播图
class Banner(models.Model):
    title=models.CharField(max_length=20)
    img=models.ImageField(upload_to='banner')
    position=models.IntegerField()#索引
    url=models.CharField(max_length=512)
    is_active=models.BooleanField(default=False)#是否活跃
    is_delete=models.BooleanField(default=False)#是否删除
    create_time=models.DateTimeField(auto_now_add=True)
    update_time=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    class Meta:
        verbose_name='轮播图'
        verbose_name_plural=verbose_name

#分类
class Category(models.Model):
    name = models.CharField(max_length=20)
    is_delete=models.BooleanField(default=False)#是否删除
    create_time=models.DateTimeField(auto_now_add=True)#创建时间
    update_time=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name='分类'
        verbose_name_plural=verbose_name

#标签
class Tags(models.Model):
    name=models.CharField(max_length=20)
    is_delete=models.BooleanField(default=False)#是否删除
    create_time=models.DateTimeField(auto_now_add=True)#创建时间
    update_time=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name='标签'
        verbose_name_plural=verbose_name


#文章
class Article(models.Model):
    title=models.CharField(max_length=100)
    content=RichTextUploadingField()
    cover=models.ImageField(upload_to='article/')
    read_num=models.IntegerField(default=0)#浏览量
    top=models.BooleanField(default=False)#置顶 推荐
    user=models.ForeignKey(BlogUser)
    category=models.ForeignKey(Category)#哪个分类
    tags=models.ManyToManyField(Tags)#哪个标签
    is_delete=models.BooleanField(default=False)#是否删除
    pub_time=models.DateTimeField(auto_now_add=True)#创建时间
    update_time=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    class Meta:
        verbose_name='文章'
        verbose_name_plural=verbose_name


#评论
class Comment(models.Model):
    content=models.CharField(max_length=200)
    article=models.ForeignKey(Article)
    user=models.ForeignKey(BlogUser)
    is_delete=models.BooleanField(default=False)#是否删除
    create_time=models.DateTimeField(auto_now_add=True)#创建时间
    update_time=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username
    class Meta:
        verbose_name='评论'
        verbose_name_plural=verbose_name


#友情链接
class FriendLink(models.Model):
    name=models.CharField(max_length=20)
    url=models.CharField(max_length=512)
    position=models.IntegerField(default=0)#索引定位
    is_delete=models.BooleanField(default=False)#是否删除
    create_time=models.DateTimeField(auto_now_add=True)#创建时间
    update_time=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name='友情链接'
        verbose_name_plural=verbose_name