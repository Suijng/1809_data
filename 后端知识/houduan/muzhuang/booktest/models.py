from django.db import models

# Create your models here.

#轮播表
class banner(models.Model):
    btitle=models.CharField(max_length=20)
    burl=models.CharField(max_length=512)
    bimage=models.ImageField(upload_to='booktst/')
    bindex=models.IntegerField()
    bcreate_time=models.DateTimeField(auto_now_add=True)
    bupdate_time=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.btitle
    class Meta:
        verbose_name = '轮播'
        verbose_name_plural = verbose_name


#文章的类型表
class type(models.Model):
    lname=models.CharField(max_length=20)

    def __str__(self):
        return self.lname
    class Meta:
        verbose_name = '文章类型'
        verbose_name_plural = verbose_name

#评论的标签表
class biaoqian(models.Model):
    bname=models.CharField(max_length=20)

    def __str__(self):
        return self.bname
    class Meta:
        verbose_name = '评论标签'
        verbose_name_plural = verbose_name
#正文表
class Article(models.Model):
    atitle=models.CharField(max_length=100)
    atime=models.DateTimeField(auto_now_add=True)
    aliulan=models.IntegerField(default=0)
    aimage=models.ImageField(upload_to='booktest')
    acontent=models.CharField(max_length=3000)
    atop=models.BooleanField(default=False)
    abupdate_time=models.DateTimeField(auto_now=True)
    alei=models.ForeignKey(type)
    abiao=models.ManyToManyField(biaoqian)

    def __str__(self):
        return self.atitle
    class Meta:
        verbose_name = '文章正文'
        verbose_name_plural = verbose_name

#评论表
class pinglun(models.Model):
    pname=models.CharField(max_length=50)
    pcontent=models.CharField(max_length=100)
    purl=models.EmailField(default=None,null=True,blank=True)
    bcreate_time=models.DateTimeField(auto_now_add=True)
    bupdate_time=models.DateTimeField(auto_now=True)
    apinglun=models.ForeignKey(Article)

    def __str__(self):
        return self.pname
    class Meta:
        verbose_name = '评论表'
        verbose_name_plural = verbose_name




