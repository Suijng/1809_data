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


import time

# 节流
VISIT_RECORD = {}
class VisitThrottle(object):

    def __init__(self):
        # 获取用户历史访问记录
        self.history = []

    # allow_request是否允许方法
    # True 允许访问
    # False 不允许访问
    def allow_request(self,request,view):
        # 1.获取用户IP
        user_ip = request._request.META.get("REMOTE_ADDR")
        key = user_ip
        print('1.user_ip------------',key)

        # 2.添加到访问记录里 创建当前时间
        createtime = time.time()
        if key not in VISIT_RECORD:
            # 当前的IP地址没有访问过服务器  没有记录 添加到字典
            VISIT_RECORD[key] = [createtime]
            return True

        # 获取当前用户所有的访问历史记录 返回列表
        visit_history = VISIT_RECORD[key]
        print('3.history==============',visit_history)
        self.history = visit_history

        # 用记录里的最有一个时间 对比 < 当前时间 -60秒
        while visit_history and visit_history[-1] < createtime-60:
            # 删除用户记录
            visit_history.pop()

        # 判断小于5秒 添加到 历史列表最前面
        if len(visit_history) < 5:
            visit_history.insert(0,createtime)
            return True

        return False # 表示访问频率过高

    def wait(self):
        first_time = self.history[-1]
        return 60-(time.time()-first_time)




# 只有登录的用户才能查看所有的用户信息
class UserList(APIView):

    # 设置节流的类
    throttle_classes = [VisitThrottle,]

    def get(self, request, *args, **kwargs):
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
