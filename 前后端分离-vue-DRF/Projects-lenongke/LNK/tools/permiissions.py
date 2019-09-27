from rest_framework import permissions

class IsOwerOrRead(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        # 对摸个对象有操权限
        if request.method in permissions.SAFE_METHODS:
            return True
        #  操作这个的用户=请求的用户
        return obj.user == request.user