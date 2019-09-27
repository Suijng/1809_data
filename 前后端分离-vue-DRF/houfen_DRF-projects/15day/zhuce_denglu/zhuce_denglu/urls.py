"""zhuce_denglu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import url,include
from django.contrib import admin
from user.views import Login,Register,UserList,Order,UserDetailView,UserListView,UserGenericAPIView

# 自动路由匹配
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
#注册路由
router.register(r'userlist',UserListView)


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^(?P<version>[v1|v2]+)/register/', Register.as_view()),
    url(r'^(?P<version>[v1|v2]+)/login/', Login.as_view()),
    # url(r'^(?P<version>[v1|v2]+)/userlist/', UserList.as_view()),
    # url(r'^(?P<version>[v1|v2]+)/userdetail/(?P<pk>\d+)/', UserDetailView.as_view(),name='userdetail'),
    # # url(r'^(?P<version>[v1|v2]+)/userdetail/\d+/', UserDetailView.as_view()),
    # url(r'^(?P<version>[v1|v2]+)/userlist111/$', UserList.as_view(),name='userlist'),
    # url(r'^(?P<version>[v1|v2]+)/users/$', UserList.as_view()),
    # url(r'^(?P<version>[v1|v2]+)/order/$', Order.as_view()),
    # 不使用自动路由匹配 URL编写方式
    url(r'^(?P<version>[v1|v2]+)/genuser/$',UserGenericAPIView.as_view({'get':'list'})),
    # url(r'^(?P<version>[v1|v2]+)/userlist/$', UserListView.as_view({'get':'list','post':'create'})),
    # url(r'^(?P<version>[v1|v2]+)/userlist/(?P<pk>\d+)/$', UserListView.as_view({'get':'retrieve','delete':'destroy','put':'update'})),
    url(r'^(?P<version>[v1|v2]+)/',include(router.urls))
]







