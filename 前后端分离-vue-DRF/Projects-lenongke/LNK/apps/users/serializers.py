import re
from datetime import datetime,timedelta
from LNK.settings import REGEX_MOBILE
from .models import VerifyCode
from rest_framework import serializers
from django.contrib.auth import get_user_model

# 获取用户model
User = get_user_model()

# 验证手机号是否合法
# 判断该手机号是否注册

# 验证码序列化
class SmsSerializers(serializers.Serializer):

    mobile = serializers.CharField(max_length=11)

    # 自定义方法验证字段
    def validate_mobile(self,value):
        # 验证手机号是否合法
        if not re.match(REGEX_MOBILE,value):
            raise serializers.ValidationError('手机号非法')

        # 判断该手机号是否注册
        if User.objects.filter(mobile=value).count():
            raise serializers.ValidationError('该用户已存在')

        # 判断验证码请求的频率(60秒发送一次)
        one_mintue_ago = datetime.now() - timedelta(days=0,minutes=2,seconds=0)

        if VerifyCode.objects.filter(add_time__gt=one_mintue_ago,mobile=value).count():
            raise serializers.ValidationError('距离上一次验证啊未超过60秒')
        return value


from rest_framework.validators import UniqueValidator

# 注册序列化
class UserRegisterSerializer(serializers.ModelSerializer):

    # 验证码
    code = serializers.CharField(
        required=True,
        max_length=4,
        min_length=4,
        write_only=True,

        error_messages={
            'blank':'请输入验证码',
            'required':'请输入验证码',
            'max_length':'验证码格式错误',
            'min_length':'验证码格式错误',
        },
        help_text = '验证码',
        label='验证码'
    )

    # 验证用户是否存在
    username = serializers.CharField(
        required=True, # 只是写入
        allow_blank=True,
        validators=[UniqueValidator(
            queryset=User.objects.all(),
            message='该用户以存在'
        )],
        help_text='用户名',
        label='用户名'
    )

    # 校验验证码
    def validate_code(self,code):
        # 在表里根据用户名 过滤
        code_history = VerifyCode.objects.filter(
            mobile=self.initial_data['username']).order_by('-add_time')

        if code_history:
            # 说明该用户获取过验证码
            last_code = code_history[0]
            # 判断验证码是否过期(5分钟)
            five_minute_ago = datetime.now() - timedelta(days=0,minutes=10,seconds=0)
            if five_minute_ago > last_code.add_time:
                raise serializers.ValidationError('验证码以过期')
            # 判断验证码是否一致
            if code != last_code.code:
                raise serializers.ValidationError('验证码错误')

        else:
            # 说明该用户没有获取过验证码
            raise serializers.ValidationError('验证码无效')
        # 验证码都通过返回验证码
        return code

    # 把用户名给手机号
    def validate(self, attrs):
        # 当所有的字段都验证通过,会经过validate方法
        attrs['mobile'] = attrs['username']
        # 移除code
        del attrs['code']

        return attrs

    # def create(self, validated_data):
    #     # user -> UserProfile()类 实例化对象
    #     user = super(UserRegisterSerializer, self).create(validated_data=validated_data)
    #     # 根据传过来的密码进行加密
    #     user.set_password(validated_data["password"])
    #     # 保存
    #     user.save()
    #     return user

    password = serializers.CharField(style={"input_type": "password"},label='密码',write_only=True)

    class Meta:
        model = User
        fields = ['username','code','mobile','password']


# 用户信息序列化  详情
class UserDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['name','gender','birthday','email','mobile']