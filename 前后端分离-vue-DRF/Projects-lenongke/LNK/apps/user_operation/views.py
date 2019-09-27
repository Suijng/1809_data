from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.mixins import CreateModelMixin,ListModelMixin,DestroyModelMixin,UpdateModelMixin
from rest_framework.viewsets import GenericViewSet

from .models import UserFav,UserLeavingMessage,UserAddress
from .serializers import UserFavSerializers,UserFavListSerializers,UserLeavingMessageSerializer,UserAddressSerializer
# 认证
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from tools.permiissions import IsOwerOrRead

# 用户操作

# 用户收藏
class UserFavViewSet(CreateModelMixin,ListModelMixin,DestroyModelMixin,GenericViewSet):

    queryset = UserFav.objects.all()
    serializer_class = UserFavSerializers
    # 权限　用户必须登录
    permission_classes = [IsAuthenticated,IsOwerOrRead]
    # 认证
    authentication_classes = [JSONWebTokenAuthentication,SessionAuthentication]

    # 搜索字段 根据商品goods_id删除
    lookup_field = 'goods_id'

    def get_serializer_class(self):
        if self.action=='list':
            # 商品收藏列表 走商品收藏序列化
            return UserFavListSerializers
        return UserFavSerializers

    # 只显示当前用户收藏
    # def get_queryset(self):
    #     # 根据当前请求的用户 过滤当前用户的收藏列表
    #     queryset = UserFav.objects.filter(user=self.request.user)
    #     return queryset


# 用户留言     # 获取 添加 删除
class UserLeavingMessageViewSet(ListModelMixin,CreateModelMixin,DestroyModelMixin,GenericViewSet):

    queryset = UserLeavingMessage
    serializer_class = UserLeavingMessageSerializer
    # 权限 用户必须登录
    permission_classes = [IsAuthenticated, IsOwerOrRead]
    # 认证
    authentication_classes = [JSONWebTokenAuthentication,SessionAuthentication]

    # 只能看到自己的留言
    def get_queryset(self):
        return UserLeavingMessage.objects.filter(user=self.request.user)



# 用户收货地址    #  增 删 改 查
class UserAddressViewSet(CreateModelMixin,DestroyModelMixin,ListModelMixin,UpdateModelMixin,GenericViewSet):

    queryset = UserAddress.objects.all()
    serializer_class = UserAddressSerializer
    # 认证
    authentication_classes = [JSONWebTokenAuthentication, SessionAuthentication]
    # 权限  用户必须登录
    permission_classes = [IsAuthenticated, IsOwerOrRead]

    # 只能看到自己的地址
    def get_queryset(self):
        return UserAddress.objects.filter(user=self.request.user)



