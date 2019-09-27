# 在原有的django的view视图基础上在封装
# 增加一些新功能
from rest_framework.views import APIView
from rest_framework.response import Response
from user import models

# Create your views here.


# 用户登录
import time, hashlib


def get_token(username, password):

    # token --> 由于当前时间,用户和密码生成,确保唯一性
    current = str(int(time.time() * 1000))
    md5_obj = hashlib.md5(current.encode('utf8'))
    md5_obj.update(username.encode('utf8'))
    md5_obj.update(password.encode('utf8'))

    return md5_obj.hexdigest()


# 注册
# class Register(APIView):
#
#     # 取消 认证 权限
#     permission_classes = []
#     authentication_classes = []
#     throttle_classes = []
#
#     def post(self, request, *args, **kwargs):
#
#         ret = {
#             'code': 1,
#             'msg': '注册成功'
#         }
#         name = request._request.POST.get('name')
#         password = request._request.POST.get('password')
#         birthday = request._request.POST.get('birthday')
#         try:
#             obj = models.User.objects.filter(name=name).first()
#
#             if obj:
#                 # 用户user import models已存在
#                 ret['code'] = 0
#                 ret['msg'] = '用户已存在'
#             else:
#                 # 用户不存在
#                 models.User.objects.create(name=name, password=password, birthday=birthday)
#                 ret['user'] = name
#
#         except Exception as e:
#             print(e)
#             ret['code'] = 0
#             ret['msg'] = '捕获异常'
#
#         return Response(ret)


# 登录
class Login(APIView):

    # 取消 认证 权限
    permission_classes = []
    authentication_classes = []
    throttle_classes = []

    def post(self, request, *args, **kwargs):

        ret = {
            'code': 1,
            'msg': '登录成功'
        }
        name = request._request.POST.get('name')
        password = request._request.POST.get('password')
        try:
            obj = models.User.objects.filter(name=name).first()
            # 1.判断是否存在
            if obj:
                # 用户已存在
                # 2.判断用户名 密码是否正确
                if obj.password == password:
                    # 登录成功
                    # 3.创建登录的标识符 (token)
                    # 生成用户登录的唯一标识,每次登录都获取新的token,
                    token = get_token(obj.name, obj.password)
                    print(token)
                    # 表中如果没有则创建数据,存在则更新数据
                    models.Token.objects.update_or_create(user=obj, defaults={'token': token})

                    # 4.返回登录后的信息 (tiken字符串)
                    # 将token登录标识返回给用户
                    ret['token'] = token

                else:
                    ret['code'] = 2
                    ret['msg'] = '用户名或密码错误'


            else:
                # 用户不存在
                ret['code'] = 1
                ret['msg'] = '该用户不存在'

        except Exception as e:
            print(e)
            ret['code'] = 0
            ret['msg'] = '捕获异常'

        return Response(ret)




from rest_framework.throttling import SimpleRateThrottle
from rest_framework.versioning import QueryParameterVersioning
from rest_framework.versioning import URLPathVersioning


# 自定义版本类
# class MyParthVersioning(object):
#     def datermint_version(self,request,*args,**kwargs):
#         # 获取用户传递的版本参数（version）
#         version = request._request.GET.get('version')
#         # version = request.query_params.get('version')
#         return version
#
#
# 只有登录的用户才能查看所有的用户信息
# class UserList(APIView):
#
#     # 设置节流的类
#     # throttle_classes = [VisitThrottle,]
#
#     # 取消节流
#     # throttle_classes = [SimpleRateThrottle]
#
#     # 设置自定义版本类
#     # versioning_class = MyParthVersioning
#     # versioning_class = QueryParameterVersioning
#     versioning_class = URLPathVersioning
#
#
#
#
#     def get(self, request, *args, **kwargs):
#
#         # request.version 版本号
#         # request.version_scheme => MyParthVersioning()
#         print(request.version,request.version_scheme)
#         #reverse反向生成url地址
#         url = request.version_scheme.reverse('userelist',request=request)
#
        # ret = {
        #     'code': 1,
        #     'msg': '请求成功'
        # }
#         try:
#             queryset = models.User.objects.all()
#
#             data = []
#             for model in queryset:
#                 cbv_d = {}
#                 cbv_d['name'] = model.name
#                 cbv_d['type'] = model.type
#                 cbv_d['birthday'] = model.birthday
#                 data.append(cbv_d)
#
#             ret['data'] = data
#
#             # 获取用户信息
#             if type(request.user) == str:
#                 user = request.user
#             else:
#                 user = request.user.name
#
#             auth = request.auth
#             ret['user'] = user
#             ret['auth'] = auth
#
#         except Exception as e:
#             print(e)
#             ret['code'] = 0
#             ret['msg'] = '捕获异常'
#
#         return Response(ret)




#######################解析器######################
from rest_framework.parsers import JSONParser,FormParser

class Order(APIView):
    permission_classes = []
    authentication_classes = []

    versioning_class = URLPathVersioning

    def post(self,request,*args,**kwargs):

        data = request.data
        print(data)

        return Response('订单接口')






##############################序列化##################################

from rest_framework import serializers

###########  注册
# class RegisterUserSerializer(serializers.Serializer):
#     # 用户名
#     name = serializers.CharField(error_messages=
#                 {
#                     'required' :'用户名不能为空'
#                 },
#
#             )
#     # 密码
#     password = serializers.CharField(error_messages=
#                 {
#                     'required' :'密码不能为空'
#                 },
#             )
#
#     # value -->password
#     def validate_password(self,value):
#         import re
#         from rest_framework.exceptions import ValidationError
#         rea = re.match(r'[A-Z]',value)
#         reb = re.search(r'[a-b]',value)
#         rec = re.search(r'[0-9]',value)
#         red = len(value)
#
#         if rea:
#             # 判断首字母大写
#             if reb and rec and red > 7:
#                 return value
#             else:
#                 raise ValidationError('密码格式错误')
#         else:
#             raise ValidationError('首字母必须大写')
#
#
#     # 创建 更新 需要自己写方法
#     def create(self, validated_data):
#         instance = models.User.objects.create(**validated_data)
#         return instance

class RegisterUserSerializer(serializers.ModelSerializer):
    # 用户名
    name = serializers.CharField(error_messages=
                {
                    'required' :'用户名不能为空'
                },

            )
    # 密码
    password = serializers.CharField(error_messages=
                {
                    'required' :'密码不能为空'
                },
            )

    # value -->password
    def validate_password(self,value):
        import re
        from rest_framework.exceptions import ValidationError
        rea = re.match(r'[A-Z]',value)
        reb = re.search(r'[a-b]',value)
        rec = re.search(r'[0-9]',value)
        red = len(value)

        if rea:
            # 判断首字母大写
            if reb and rec and red > 7:
                return value
            else:
                raise ValidationError('密码格式错误')
        else:
            raise ValidationError('首字母必须大写')

    class Meta:
        pass
        # model = models.User



class Register(APIView):

    def post(self, request, *args, **kwargs):

        ret = {
            'code': 1,
            'msg': '注册成功'
        }

        # .data使用了解析器
        data = request.data
        # 进行序列化
        ser = RegisterUserSerializer(data=data)
        if ser.is_valid(): # 进行序列化验证
            print(ser.validated_data)
            # 保存验证后的数据(保存到数据库)
            ser.save()
        else:
            # 未通过验证
            print(ser.errors)
            ret['code'] = 0
            ret['msg'] = '注册失败'

        return Response(ret)




########### 用户列表
class UserSerializer(serializers.Serializer):
    # id
    # id = serializers.IntegerField()
    url = serializers.HyperlinkedIdentityField(
        view_name='userdetail',lookup_field='id',
        lookup_url_kwarg='pk'
    )
    # 用户名
    name = serializers.CharField()
    # 用户类型 (普通类型,VIP类型)
    # type = serializers.IntegerField()
    type = serializers.CharField(source='get_type_display')



###########  分页
# DRF 提供了三种方式
from rest_framework.pagination import PageNumberPagination
# https://www.baidu.com/?kw=xxx&page=1&pagessize=10
# 自定义分类
class MpPageNumberPagination(PageNumberPagination):
    # page_size 每页返回多少条数
    page_size = 5
    # 传递分页的参数
    page_query_param = 'page'
    # 传递每页返回多少数据的参数
    page_size_query_param = 'pagesize'
    # 每页返回数据的最大条数
    max_page_size = 10

    def get_paginated_response(self, data):
        ret = {
            'code':1,
            'count':self.page.paginator.count,
            'previous':self.get_previous_link(),
            'results': data
        }
        return Response(ret)


# https://www.baidu.com/?kw=xxx&page=1&pagessize=10



from  django.forms import model_to_dict
from util.authentication import MyBaseAuthentication

class UserList(APIView):

    # authentication_classes =[MyBaseAuthentication]

    def get(self,request,*args,**kwargs):

        ret = {
            'code': 1,
            'data': None
        }

        # 获取用户列表
        queryset = models.User.objects.all()

        # 实例化分页类
        pg = MpPageNumberPagination()
        pg_data = pg.paginate_queryset(queryset=queryset,request=request,view=self)

        # 实例化一个对象 把取出来的model序列化
        ser = UserSerializer(
            instance=pg_data,
            context={'request',request},
            many=True)

        # ret['data'] = ser.data
        # return Response(ret)
        return pg.get_paginated_response(ser.data)

        # queryset = models.User.objects.all('id','user','type')
        # print(type(queryset))
        # data = list(queryset)
        # print(data)




########## 用户详情
class UserDetailSerializer(serializers.Serializer):
    # id
    id = serializers.IntegerField()
    # 用户名
    name = serializers.CharField()
    # 用户类型 (普通类型,VIP类型)
    # type = serializers.IntegerField()
    type = serializers.CharField(source='get_type_display')
    # 密码
    password = serializers.CharField()
    # 性别
    # gender = serializers.IntegerField()
    gender = serializers.CharField(source='get_gender_display')
    # 出生日期
    birthday = serializers.DateTimeField(format='%Y-%m-%d')



class UserDetailView(APIView):

    def get(self,request,*args,**kwargs):

        ret = {
            'code': 1,
            'data': None
        }

        # id = int(request._request.GET.get('id'))
        id = kwargs.get('pk')
        quertset = models.User.objects.filter(id=id).first()

        try:
            if quertset:
                # 用户存在
                # 序列化
                ser = UserDetailSerializer(instance=quertset,many=False)
                ret['data'] = ser.data
            else:
                ret['code'] = 0
                ret['msg'] = '用户不存在'

        except Exception as e:
            print(e)
            ret['code'] = 0
            ret['msg'] = '用户不存在'

        return Response(ret)















