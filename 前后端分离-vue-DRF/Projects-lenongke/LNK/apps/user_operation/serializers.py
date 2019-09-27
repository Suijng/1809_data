from .models import UserFav,UserLeavingMessage,UserAddress
from rest_framework import serializers
# 联合唯一的验证
from rest_framework.validators import UniqueTogetherValidator


# 用户收藏序列化
class UserFavSerializers(serializers.ModelSerializer):

    # 获取当前登录的用户
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    # add_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M')

    class Meta:
        # 确保用户收藏一个商品只能收藏一次
        validators = [UniqueTogetherValidator(
            queryset=UserFav.objects.all(),
            fields=('user','goods'),
            message='该商品已收藏'
        )]
        model = UserFav
        fields = ['user','goods','id']
        # fields = '__all__'


# 展示商品序列化
from goods.serializers import GoodsSerializers

class UserFavListSerializers(serializers.ModelSerializer):
    goods = GoodsSerializers()

    class Meta:
        model = UserFav
        fields = '__all__'


# 用户留言序列化
class UserLeavingMessageSerializer(serializers.ModelSerializer):
    # 获取当前登录的用户
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    add_time = serializers.DateTimeField('%Y-%m-%d %H:%M',read_only=True)

    class Meta:

        model = UserLeavingMessage
        # fields = ['user','message_type','subject','message','file','add_time']
        fields = '__all__'


# 收货地址
class UserAddressSerializer(serializers.ModelSerializer):
    # 获取当前登录的用户
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = UserAddress
        fields = ['id','user', 'province', 'city', 'district', 'address','signer_name','signer_mobile']


'''
    user = models.ForeignKey(User, verbose_name="用户")
    province = models.CharField(max_length=100, default="", verbose_name="省份")
    city = models.CharField(max_length=100, default="", verbose_name="城市")
    district = models.CharField(max_length=100, default="", verbose_name="区域")
    address = models.CharField(max_length=100, default="", verbose_name="详细地址")
    signer_name = models.CharField(max_length=100, default="", verbose_name="签收人")
    signer_mobile = models.CharField(max_length=11, default="", verbose_name="电话")
'''