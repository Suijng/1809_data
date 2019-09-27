from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from user import models


# 认证类部分
class MyBaseAuthentication(BaseAuthentication):

    def authenticate(self, request):
        # 实现认证逻辑,判断用户是否登录
        token = request._request.GET.get('token')
        print(token)
        token_obj = models.Token.objects.filter(token=token).first()

        if token_obj:
            # 用户已经登录
            # user       auth
            return (token_obj.user, token)

        else:
            raise AuthenticationFailed('认证失败,用户未登录')



    # authentication_classes = [MyBaseAuthentication,]



