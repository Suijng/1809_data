from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

#分类
class Tag(models.Model):
    name=models.CharField(max_length=50)
    is_delete=models.BooleanField(default=False)#是否删除
    create_time=models.DateTimeField(auto_now_add=True)#创建时间
    update_time=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name='分类'
        verbose_name_plural=verbose_name

#文章
class Article(models.Model):
    title = models.CharField(max_length=100)
    content = RichTextUploadingField()
    top = models.BooleanField(default=False)#推荐笑话
    read_num=models.IntegerField(default=0)#浏览量
    index = models.IntegerField()#索引
    tag = models.ForeignKey(Tag)  # 哪个分类
    pub_time=models.DateTimeField(auto_now_add=True)#创建时间
    update_time=models.DateTimeField(auto_now=True)#更新时间
    is_delete=models.BooleanField(default=False)#是否删除

    def __str__(self):
        return self.title
    class Meta:
        verbose_name='文章'
        verbose_name_plural=verbose_name

#