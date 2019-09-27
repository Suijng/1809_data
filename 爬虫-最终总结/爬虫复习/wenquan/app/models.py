from django.db import models

# Create your models here.

# 轮播图
class Banner(models.Model):
    # 标题
    title = models.CharField(max_length=50,default=None)
    # 图片
    img = models.ImageField(upload_to='banner/')
    # 网址
    url = models.CharField(max_length=512,default=None)
    # 索引
    index = models.IntegerField()
    # 创建时间
    create_time = models.DateTimeField(auto_now_add=True)
    # 更新时间
    update_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


# 正文
class Article(models.Model):
    # 标题
    name = models.CharField(max_length=100)
    # 内容
    content = models.CharField(max_length=3000)
    # 时间
    time_info = models.CharField(max_length=50)
    # 图片  默认为空 可以不上传
    img = models.ImageField(upload_to='blog/', default=None, null=True, blank=True)
    # 创建时间
    create_time = models.DateTimeField(auto_now_add=True)
    # 更新时间
    update_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


# 预定房间
class YuDing(models.Model):
    # 名字
    name = models.CharField(max_length=100)
    # 面积
    mianji = models.CharField(max_length=100)
    # 名称
    img = models.ImageField(upload_to='yuding/', default=None, null=True, blank=True)
    # 入住时间
    ruzhutime = models.CharField(max_length=100)
    # 离店时间
    lidiantime = models.CharField(max_length=100)
    # 创建时间
    create_time = models.DateTimeField(auto_now_add=True)
    # 更新时间
    update_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


# 房间下详情
class FangJian(models.Model):
    # 名称
    name = models.CharField(max_length=100)
    # 房价
    fangjia = models.CharField(max_length=50)
    # 备注
    beizhu = models.CharField(max_length=100)
    # 支付方式
    zhifu = models.CharField(max_length=60)
    # 那个房间的
    yuding = models.ForeignKey(YuDing)
    # 创建时间
    create_time = models.DateTimeField(auto_now_add=True)
    # 更新时间
    update_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


# 登录
class Login(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.username