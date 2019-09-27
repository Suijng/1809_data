"""LNK URL Configuration

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
import xadmin
from django.views.static import serve
from LNK.settings import MEDIA_ROOT
from goods import views as good_views
from users import views as user_views
from user_operation import views as user_o_views
from trade import views as trade_views

from rest_framework.routers import DefaultRouter
# 登录生成token
from rest_framework.authtoken import views
# jwk方式生成唯一标识
from rest_framework_jwt.views import obtain_jwt_token

router = DefaultRouter()
# 商品列表
router.register(r'goods',good_views.GoodsListView,base_name='goods')
# 分类列表
router.register(r'categorys',good_views.GoodsCategoryView,base_name='categorys')
# 首页轮播图
router.register(r'banner',good_views.BannerViewset,base_name='getBanner')
#  热搜词
router.register(r'hotsearchs',good_views.HotSearchWordsViewset,base_name='hotsearchs')
# 获取首页商品下方
router.register(r'indexgoods',good_views.IndexCategiryViewSet,base_name='indexgoods')


# 配置验证码接口
router.register(r'code',user_views.SmsViewSet,base_name='code')
# 注册
router.register(r'users',user_views.UserViewSet,base_name='users')


# 用户收藏接口
router.register(r'userfavs',user_o_views.UserFavViewSet,base_name='userfavs')
# 用户留言接口
router.register(r'messages',user_o_views.UserLeavingMessageViewSet,base_name='messages')
# 用户的收货地址
router.register(r'address',user_o_views.UserAddressViewSet,base_name='address')


# 购物车接口
router.register(r'shopcarts',trade_views.ShopCartViewSet,base_name='shopcarts')
# 订单接口
router.register(r'orders',trade_views.OrderInfoViewSet,base_name='orders')


from rest_framework.documentation import include_docs_urls


urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^xadmin/',xadmin.site.urls),
    url(r'^ueditor/',include('DjangoUeditor.urls')),
    # 配置图片路径
    url(r'^media/(?P<path>.*)$',serve,{'document_root':MEDIA_ROOT}),
    # 商品列表
    # url(r'^api/(?P<version>[v1|v2]+)/goodslist/$',good_views.GoodsListView.as_view({'get':'list'})),
    url(r'^api/',include(router.urls)),
    # url(r'^api/login/',views.obtain_auth_token), # 等价于视图
    url(r'^api/login/', obtain_jwt_token),
    # http://127.0.0.1:8000/api/ailpay/return
    url(r'^api/ailpay/return/',trade_views.AlipayView.as_view()),
    url(r'^api/docs/',include_docs_urls(title='乐农客'))
]
