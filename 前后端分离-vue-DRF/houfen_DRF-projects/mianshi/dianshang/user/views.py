from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from user.serializers import RegisterUserSerializer, CategorySerializer, \
    ClothesSerializer, ShopcarSerializer, AddressSerializer, \
    ClothesListSerializer,ShopcarAddSerializer
from user.models import User, Token, Category, Clothes, Shopcar, Address

from utils.pagination import MyPageNumberPagination
from utils.authentication import MyBaseAuthentication

from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin, ListModelMixin, \
    RetrieveModelMixin, DestroyModelMixin
from rest_framework import status


# **********************   注册clothes
class RegisterView(CreateModelMixin, GenericViewSet):
    queryset = User.objects.all()
    serializer_class = RegisterUserSerializer



    # 重写内部方法
    def create(self, request, *args, **kwargs):
        ret = {
            'code': 1,
            'msg': '注册成功'
        }
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(ret, status=status.HTTP_201_CREATED, headers=headers)
        else:
            # 验证失败打印错误信息
            print(serializer.errors)
            ret['code'] = 0
            ret['msg'] = '参数错误,注册失败'
            return Response(ret)



# **********************   登录

# 生成token
import time, hashlib


def get_token(name, password):
    add_time = str(int(time.time() * 1000))
    md5_obj = hashlib.md5(add_time.encode('utf8'))
    md5_obj.update(name.encode('utf8'))
    md5_obj.update(password.encode('utf8'))

    return md5_obj.hexdigest()


# 登录
class LoginView(APIView):

    def post(self, request, *args, **kwargs):
        ret = {
            'code': 1,
            'msg': '登录成功'
        }

        # 获取post请求
        data = request.data
        # 获取用户名
        name = data['name']
        # 获取密码
        password = data['password']
        try:
            obj = User.objects.filter(name=name).first()
            if obj:
                # 用户存在的
                if obj.password == password:
                    # 登录成功了 登录成功的标识
                    token = get_token(name, password)
                    Token.objects.update_or_create(user=obj, defaults={'token': token})
                    ret['token'] = token
                else:
                    # 密码错误
                    ret['msg'] = '账号或密码错误'
                    ret['code'] = 0
            else:
                ret['msg'] = '该用户不存在'
                ret['code'] = 0

        except Exception as e:
            print(e)
            ret['msg'] = '捕获登录异常'
            ret['code'] = 0

        return Response(ret)


# *****************  分类展示
class CategoryView(ListModelMixin, RetrieveModelMixin, GenericViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = MyPageNumberPagination

    def get_serializer_class(self):
        # 动态设置序列化的类
        if self.action == 'list':
            return CategorySerializer
        elif self.action == 'retrieve':
            return ClothesListSerializer

    def list(self, request, *args, **kwargs):
        ret = {
            'code': 1,
        }
        queryset = self.filter_queryset(self.get_queryset())
        # 没有分页展示所有数据
        serializer = self.get_serializer(queryset, many=True)
        ret['data'] = serializer.data
        return Response(ret)

    def retrieve(self, request, *args, **kwargs):
        category_id = kwargs.get('pk')
        if category_id:
            clothes = Clothes.objects.filter(category=category_id)
            page = self.paginate_queryset(clothes)
            # 找到要分页的数据
            if page is not None:
                serializer = self.get_serializer(page, many=True)
                return self.get_paginated_response(serializer.data)



# ********************  商品详情
class ClothesView(RetrieveModelMixin, GenericViewSet):
    queryset = Clothes.objects.all()
    serializer_class = ClothesSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        ret = {'code': 1, 'data': serializer.data}
        return Response(ret)



# *******************  购物车
class ShopcarView(CreateModelMixin, ListModelMixin, DestroyModelMixin, GenericViewSet):
    queryset = Shopcar.objects.all()
    serializer_class = ShopcarSerializer

    authentication_classes = [MyBaseAuthentication]

    def get_serializer_class(self):
        # 动态设置序列化的类
        if self.action == 'list':
            return ShopcarSerializer
        elif self.action == 'create':
            return ShopcarAddSerializer

    def create(self, request, *args, **kwargs):
        ret = {
            'code': 1,
            'msg': '添加成功'
        }
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(ret, status=status.HTTP_201_CREATED, headers=headers)
        else:
            # 验证失败打印错误信息
            print(serializer.errors)
            ret['code'] = 0
            ret['msg'] = '参数错误,添加失败'
            return Response(ret)


    def list(self, request, *args, **kwargs):
        user_id = request.user.id
        queryset = Shopcar.objects.filter(user=user_id)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


    def destroy(self, request, *args, **kwargs):
        shop_id = kwargs.get('pk')
        print(shop_id)
        if shop_id:
            shop = Shopcar.objects.filter(id=shop_id)
            self.perform_destroy(shop)
            return Response(status=status.HTTP_204_NO_CONTENT)


# ******************  地址
class AddressView(RetrieveModelMixin,ListModelMixin,GenericViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

    authentication_classes = [MyBaseAuthentication]

    def list(self, request, *args, **kwargs):
        user_id = request.user.id
        queryset = Address.objects.filter(user=user_id)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
