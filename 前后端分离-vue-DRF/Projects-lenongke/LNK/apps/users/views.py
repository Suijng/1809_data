from django.shortcuts import render

# Create your views here.

from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model  # 获取全局配置
from django.db.models import Q  # 表示筛选

from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin,UpdateModelMixin
from rest_framework.response import Response
from rest_framework import status
from tools.yunpian import YunPian
from LNK.settings import APIKEY
from .serializers import SmsSerializers, UserRegisterSerializer,UserDetailSerializer
from .models import VerifyCode
from random import choice
# 认证
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.authentication import SessionAuthentication
from tools.permiissions import IsOwerOrRead
from rest_framework.permissions import IsAuthenticated

# 因为当前登录可以通过手机号页可以通过账号登录

# 获取用户model类
User = get_user_model()


# 自定义用户认证
class CustomBackend(ModelBackend):

    def authenticate(self, request, username=None, password=None, **kwargs):
        # username前端传过来的  既可以是手机号,也可以是账号
        # 用户名和手机号都可以登录
        try:
            user = User.objects.get(
                Q(username=username, ) |
                Q(mobile=username)
            )
            # 检测用户输入的密码是否正确
            if user.check_password(password):
                return user
        except Exception as e:
            print(e)
            return None


# 注册
class SmsViewSet(CreateModelMixin, GenericViewSet):
    # 验证手机号
    serializer_class = SmsSerializers

    # 生成验证码
    def get_code(self):
        # 生成4位验证码
        code_str = '0123456789'
        codes = []
        for i in range(4):
            code = choice(code_str)
            codes.append(code)
        return ''.join(codes)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # 获取手机号
        mobile = serializer.validated_data['mobile']
        yun_pian = YunPian(APIKEY)
        code = self.get_code()
        ret = yun_pian.send_sms(code, mobile)
        if ret['code'] != 0:
            return Response(
                {'mobile': mobile, 'msg': ret['msg']},
                status=status.HTTP_400_BAD_REQUEST
            )
        else:
            # 验证码发送成功
            code_verify = VerifyCode(code=code, mobile=mobile)
            # 保存
            code_verify.save()
            return Response(
                {'code': code, 'msg': ret['msg'], },
                status=status.HTTP_201_CREATED
            )


# 验证码
from rest_framework_jwt.utils import jwt_encode_handler, jwt_payload_handler


# 头部 负载 签名(防止用户篡改)
class UserViewSet(CreateModelMixin, RetrieveModelMixin,UpdateModelMixin,GenericViewSet):
    serializer_class = UserRegisterSerializer
    queryset = User.objects.all()
    # 认证
    authentication_classes = [JSONWebTokenAuthentication, SessionAuthentication]

    # 哪个序列化
    def get_serializer_class(self):
        if self.action == "create":
            # 创建用户接口
            return UserRegisterSerializer

        return UserDetailSerializer

    # 权限
    def get_permissions(self):
        if self.action == "create":
            return []
        #                      登录后才能访问
        return [IsOwerOrRead(),IsAuthenticated()]
    # 哪个用户的
    def get_object(self):
        return self.request.user


    def create(self, request, *args, **kwargs):
        # 序列化 将数据保存到数据库里
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.perform_create(serializer)

        # 生成token并返回
        re_dict = {}
        # re_dict = serializer.data
        payload = jwt_payload_handler(user)
        re_dict["token"] = jwt_encode_handler(payload)
        re_dict["name"] = user.name if user.name else user.username

        headers = self.get_success_headers(serializer.data)
        return Response(re_dict, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        return serializer.save()
