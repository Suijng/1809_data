from django.shortcuts import render
from django.http.response import HttpResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt,csrf_protect # 免去 添加CSRF认证
from django.utils.decorators import method_decorator


# Create your views here.

#########################FBV#########################
# 没有设置全局 要添加CSRF认证 csrf_protect
# 设置了全局 要免除CSRF认证 csrf_exempt
# @csrf_exempt
# @csrf_protect
def user(requset):
    if requset.method == 'GET':
        return HttpResponse('FBV GET')

    elif requset.method == 'POST':
        return HttpResponse('FBV POST')

    elif requset.method == 'DELETE':
        return HttpResponse('FBV DELETE')

    elif requset.method == 'PUT':
        return HttpResponse('FBV PUT')




#########################CBV#########################
class BaseView(object):
    @method_decorator(csrf_exempt) # 重写dispatch方法 添加装饰器

    def dispatch(self,request,*args,**kwargs):
        # 找到请求方法对应的函数(反射)
        print('请求即将执行')

        # 调用父类的dispatch方法
        result = super(BaseView,self).dispatch(self,request,*args,**kwargs)
        print('请求执行完毕')
        return result

@method_decorator(csrf_exempt,name='dispatch') # 指定def函数名称
class User(View):

    def get(self,request,*args,**kwargs):
        print('执行GET请求')
        return HttpResponse('CBV GET')

    def post(self,request,*args,**kwargs):
        return HttpResponse('CBV POST')

    def delete(self,request,*args,**kwargs):
        return HttpResponse('CBV DELETE')

    def put(self,request,*args,**kwargs):
        return HttpResponse('CBV PUT')


class Student(BaseView,View):

    def get(self,request,*args,**kwargs):
        return HttpResponse('CBV GET')

    def post(self,request,*args,**kwargs):
        return HttpResponse('CBV POST')

    def delete(self,request,*args,**kwargs):
        return HttpResponse('CBV DELETE')

    def put(self,request,*args,**kwargs):
        return HttpResponse('CBV PUT')






# 在原有的django的view视图基础上在封装
# 增加一些新功能
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.authentication import BaseAuthentication


# class Myauthentication(BaseAuthentication):
#
#     def authenticate(self, request):
#
#         # 实现认证逻辑,判断用户是否登录
#         token = request._request.GET.get('token')
#         if token and token == '123':
#             print('------------')
#             # 用户登录成功
#             return ('lisi', token)
#
#         else:
#             raise AuthenticationFailed('认证失败')
#
#     def authenticate_header(self, request):
#         pass




class Myauthentication(BaseAuthentication):

    def authenticate(self,request):

        # 实现认证逻辑,判断用户是否登录
        token = request._request.GET.get('token')
        if token and token == '123':
            print('------登录成功------')
            # 用户登录成功
            return ('lisi',token)

        else:
            raise AuthenticationFailed('认证失败')


class RestUser(APIView):

    # 设置认证类
    authentication_classes = [Myauthentication,]

    ret = {
        'code':1,
        'msg':None
    }

    def get(self,request,*args,**kwargs):
        self.ret['msg'] = 'GET请求'
        return Response(self.ret)

    def post(self,request,*args,**kwargs):
        self.ret['msg'] = 'POST请求'
        return Response(self.ret)

    def delete(self,request,*args,**kwargs):
        self.ret['msg'] = 'DELETE请求'
        return Response(self.ret)

    def put(self,request,*args,**kwargs):
        self.ret['msg'] = 'PUT请求'
        return Response(self.ret)




















