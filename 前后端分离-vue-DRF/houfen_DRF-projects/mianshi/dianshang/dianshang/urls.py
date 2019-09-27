"""dianshang URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from user.views import RegisterView,LoginView,CategoryView,ShopcarView,AddressView,ClothesView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # 注册接口
    url(r'^api/(?P<version>[v1|v2]+)/register/$',RegisterView.as_view({'post':'create'})),
    # 登录接口
    url(r'^api/(?P<version>[v1|v2]+)/login/$',LoginView.as_view()),
    # 分类列表页
    url(r'^api/(?P<version>[v1|v2]+)/category/$',CategoryView.as_view({'get':'list'})),
    # 根据分类id 获取某个分类下的所有商品
    url(r'^api/(?P<version>[v1|v2]+)/category/(?P<pk>\d+)/$',CategoryView.as_view({'get':'retrieve'}),name='category'),
    # 某个商品的详情
    url(r'^api/(?P<version>[v1|v2]+)/clothes/(?P<pk>\d+)/$',ClothesView.as_view({'get':'retrieve'}),name='clothes'),
    # 添加购物车接口
    url(r'^api/(?P<version>[v1|v2]+)/addshopcar/$',ShopcarView.as_view({'post':'create'}),name='addshopcar'),
    # 购物车接口
    url(r'^api/(?P<version>[v1|v2]+)/shopcar/$',ShopcarView.as_view({'get':'list'}),name='shopcar'),
    # 删除购物车
    url(r'^api/(?P<version>[v1|v2]+)/shopcar/(?P<pk>\d+)/$',ShopcarView.as_view({'delete':'destroy'})),
    # 地址接口
    url(r'^api/(?P<version>[v1|v2]+)/address/$',AddressView.as_view({'get':'list'}),name='address'),
]


