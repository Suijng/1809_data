from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from user.serializers import ResgsterUserSerializer,CategorySerializer,\
    BookDetailSerializer,BookSerializer,\
    ChpaterListSerializer,ChpaterDetailSerializer
from user.models import User,Token,Category,Book,Chpater

from utils.pagination import MyPageNumberPagination

# 注册
# class RegisterView(APIView):
#
#     def post(self,request,*args,**kwargs):
#         ret = {
#             'code':1,
#             'msg':'注册成功'
#         }
#         # 获取post请求参数
#         data = request.data
#         # 序列化请求参数
#         ser = ResgsterUserSerializer(data=data)
#         if ser.is_valid(): # 验证字段
#             print(ser.validated_data)
#             ser.save()
#         else:
#             # 验证失败打印错误信息
#             print(ser.errors)
#             ret['code'] = 0
#             ret['msg'] = '参数错误,注册失败'
#
#         return Response(ret)


from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin,ListModelMixin,RetrieveModelMixin
from rest_framework import status

# 注册
class RegisterView(CreateModelMixin,GenericViewSet):
    queryset = User.objects.all()
    serializer_class = ResgsterUserSerializer

    # 重写内部创建方法
    def create(self, request, *args, **kwargs):
        ret = {
            'code': 1,
            'msg': '注册成功'
        }
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(ret,status=status.HTTP_201_CREATED, headers=headers)
        else:
            # 验证失败打印错误信息
            print(serializer.errors)
            ret['code'] = 0
            ret['msg'] = '参数错误,注册失败'
            return Response(ret)


#**************************  登录

# 生成token
import time,hashlib

def get_token(name,password):

    add_time = str(int(time.time() * 1000))
    md5_obj = hashlib.md5(add_time.encode('utf8'))
    md5_obj.update(name.encode('utf8'))
    md5_obj.update(password.encode('utf8'))

    return md5_obj.hexdigest()


# 登录
class LoginView(APIView):

    def post(self,request,*args,**kwargs):
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
                    # 登录成功 生成登录标识
                    token = get_token(name,password)
                    Token.objects.update_or_create(user=obj,defaults={'token':token})
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
            ret['msg'] = '捕获异常'
            ret['code'] = 0

        return Response(ret)



#******************  书籍分类
class CategoryView(ListModelMixin,RetrieveModelMixin,GenericViewSet):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = MyPageNumberPagination

    def get_serializer_class(self):
        # 动态设置序列化的类
        if self.action == 'list':
            return CategorySerializer
        elif self.action == 'retrieve':
            return BookSerializer

    # 给前端展示的字典套列表套字典
    def list(self, request, *args, **kwargs):
        print(request.version) # 打印版本
        ret = {
            'code': 1,
        }
        queryset = self.filter_queryset(self.get_queryset())
        # 没有分页展示所有数据
        serializer = self.get_serializer(queryset, many=True)
        ret['data'] = serializer.data
        return Response(ret)

    #***** 书籍分类下的书
    def retrieve(self, request, *args, **kwargs):
        category_id = kwargs.get('pk')
        if category_id:
            books = Book.objects.filter(category=category_id)
            # 调用paginate_queryset方法获取当前分页数据
            page = self.paginate_queryset(books)
            # 通过判断page结果 判断是否使用了分页
            if page is not None:
                serializer = self.get_serializer(page,many=True)
                return self.get_paginated_response(serializer.data)


#********  书籍详情视图  获取每本book书的url地址
class BookDetailView(RetrieveModelMixin,GenericViewSet):

    queryset = Book.objects.all()
    serializer_class = BookDetailSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        ret = {'code':1,'data':serializer.data}
        return Response(ret)


# 章节列表视图
from utils.authenandpermission import MyPermission,MyAuthentication

class ChapterView(ListModelMixin,RetrieveModelMixin,GenericViewSet):

    queryset = Chpater.objects.all()
    serializer_class = ChpaterListSerializer
    pagination_class = MyPageNumberPagination

    def get_serializer_class(self):
        if self.action == 'list':
            return ChpaterListSerializer
        elif self.action == 'retrieve':
            return ChpaterDetailSerializer

    # 认证
    def get_authenticators(self):
        if self.kwargs.get('pk'):
            # 根据章节id获取，章节详情
            return [MyAuthentication(),]
        return []

    # 权限
    def get_permissions(self):
        if self.kwargs.get('pk'):
            # 根据章节id获取，章节详情，返回权限类
            return [MyPermission(), ]
        return []

    def list(self, request, *args, **kwargs):
        book_id = kwargs.get('bookid')
        if book_id:
            chpaters = Chpater.objects.filter(book=book_id)
            # 调用paginate_queryset方法获取当前分页数据
            page = self.paginate_queryset(chpaters)
            # 通过判断page结果 判断是否使用了分页
            if page is not None:
                serializer = self.get_serializer(page, many=True)
                return self.get_paginated_response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        # 根据章节的id获取章节详情信息
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        ret = {'code':1,'data':serializer.data}
        return Response(ret)



