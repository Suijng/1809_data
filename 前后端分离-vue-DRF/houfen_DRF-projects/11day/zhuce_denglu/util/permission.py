# 权限类部分
from rest_framework.permissions import BasePermission

class MyPermission(BasePermission):

    message = 'vip用户才能访问'

    def has_permission(self,request,view):
        if request.user.type == 1:
            # type==1 表示vip用户
            return True

        return False



    # permission_classes = [MyPermission,]

# class MyPermission(object):
#
#     message = 'vip用户才能访问'
#     def has_permission(self,request,view):
#         if request.user.type == 1:
#             # type==1 表示vip用户
#             return True
#
#         return False

