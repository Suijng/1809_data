from .models import Schools
from rest_framework import serializers


# 学校列表序列化
class SchoolSerializers(serializers.ModelSerializer):
    urls = serializers.HyperlinkedIdentityField(
        view_name='schooldetail',
        lookup_field='id',
        lookup_url_kwarg='pk'
    )

    name = serializers.CharField(max_length=56)  # 学校名
    url = serializers.CharField(max_length=256)  # 学校logo
    tese = serializers.CharField(max_length=56)  # 特色 211 985
    lishu = serializers.CharField(max_length=56)  # 隶属
    suozaidi = serializers.CharField(max_length=56)  # 所在地
    wangzhi = serializers.CharField(max_length=256)  # 网址
    xingzhi = serializers.CharField(max_length=30)  # 性质 本科
    leixing = serializers.CharField(max_length=20) # 类型 综合 工本

    class Meta:
        model = Schools
        fields = ['id','name','url','tese','lishu','suozaidi','wangzhi','xingzhi','leixing','urls']


# 学校详情接口
class SchoolDetailSerializers(serializers.ModelSerializer):

    name = serializers.CharField(max_length=56)  # 学校名
    url = serializers.CharField(max_length=256)  # 学校logo
    tese = serializers.CharField(max_length=56)  # 特色 211 985
    lishu = serializers.CharField(max_length=56)  # 隶属
    suozaidi = serializers.CharField(max_length=56)  # 所在地
    yuanshi = serializers.CharField(max_length=56)  # 院士
    boshi = serializers.CharField(max_length=56)  # 博士
    shuoshi = serializers.CharField(max_length=56)  # 硕士
    address = serializers.CharField(max_length=126)  # 地址
    phone = serializers.CharField(max_length=20)  # 电话
    email = serializers.CharField(max_length=30)  # 邮箱
    wangzhi = serializers.CharField(max_length=256)  # 网址

    class Meta:
        model = Schools
        fields = ['id','name','url','tese','lishu','suozaidi','yuanshi','boshi','shuoshi','address','phone','email','wangzhi']


