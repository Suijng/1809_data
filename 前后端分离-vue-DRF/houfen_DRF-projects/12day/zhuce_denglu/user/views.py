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
class Register(APIView):

    # 取消 认证 权限
    permission_classes = []
    authentication_classes = []
    throttle_classes = []

    def post(self, request, *args, **kwargs):

        ret = {
            'code': 1,
            'msg': '注册成功'
        }
        name = request._request.POST.get('name')
        password = request._request.POST.get('password')
        birthday = request._request.POST.get('birthday')
        try:
            obj = models.User.objects.filter(name=name).first()

            if obj:
                # 用户user import models已存在
                ret['code'] = 0
                ret['msg'] = '用户已存在'
            else:
                # 用户不存在
                models.User.objects.create(name=name, password=password, birthday=birthday)
                ret['user'] = name

        except Exception as e:
            print(e)
            ret['code'] = 0
            ret['msg'] = '捕获异常'

        return Response(ret)


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


# 只有登录的用户才能查看所有的用户信息
class UserList(APIView):

    # 设置节流的类
    # throttle_classes = [VisitThrottle,]

    # 取消节流
    # throttle_classes = [SimpleRateThrottle]

    # 设置自定义版本类
    # versioning_class = MyParthVersioning
    # versioning_class = QueryParameterVersioning
    versioning_class = URLPathVersioning




    def get(self, request, *args, **kwargs):

        # request.version 版本号
        # request.version_scheme => MyParthVersioning()
        print(request.version,request.version_scheme)
        #reverse反向生成url地址
        url = request.version_scheme.reverse('userelist',request=request)

        ret = {
            'code': 1,
            'msg': '请求成功'
        }
        try:
            queryset = models.User.objects.all()

            data = []
            for model in queryset:
                cbv_d = {}
                cbv_d['name'] = model.name
                cbv_d['type'] = model.type
                cbv_d['birthday'] = model.birthday
                data.append(cbv_d)

            ret['data'] = data

            # 获取用户信息
            if type(request.user) == str:
                user = request.user
            else:
                user = request.user.name

            auth = request.auth
            ret['user'] = user
            ret['auth'] = auth

        except Exception as e:
            print(e)
            ret['code'] = 0
            ret['msg'] = '捕获异常'

        return Response(ret)
