from rest_framework.authentication import BaseAuthentication
from rest_framework.permissions import BasePermission
from user.models import Token,Chpater
from rest_framework.exceptions import AuthenticationFailed

class MyAuthentication(BaseAuthentication):

    def authenticate(self, request):
        # 在这里实现认证逻辑
        token = request._request.GET.get('token')
        obj = Token.objects.filter(token=token).first()

        if obj:
            #用户已登录
            ##      user    auth
            return (obj.user,token)
        else:
            raise AuthenticationFailed('用户未登录')


class MyPermission(BasePermission):
    message = '该章节为vip章节'
    def has_permission(self, request, view):
        #第一判断当前访问的章节是否是vip章节
        chpater_id = view.kwargs['pk']
        obj = Chpater.objects.filter(id=chpater_id).first()

        #判断章节是否是vip章节
        if obj.chvip:
            #判断用户是否是vip用户
            if request.user.type == 1:
                return True
            else:
                return False

        return True








