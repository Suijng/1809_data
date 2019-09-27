from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$',views.index),
    url(r'^index/$',views.index),

    url(r'^user/$',views.user),
    url(r'^good/$',views.good),
    url(r'^user1/$',views.user1),
    url(r'^user2/$',views.user2),

    #转义
    url(r'^html_escape/$',views.html_escape),
    url(r'^csrf1/$',views.csrf1),
    #登录 验证码
    url(r'^verify_code/',views.verify_code),
    url(r'^login/$',views.login),
    #反向解析
    url(r'^fan1',views.fan1),
    url(r'^fan2',views.fan2,name='fan2'),
    #位置参数
    url(r'^fan3/(\d+)_(\d+)/$',views.fan3,name='fan3'),
    #关键字参数
    url(r'^fan4/(?P<num>\d+)_(?P<num1>\d+)/$',views.fan4,name='fan4'),

    url(r'^fan5/(\d+)_(\d+)',views.fan5,name='fan5'),
]