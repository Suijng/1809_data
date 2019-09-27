from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$',views.index),
    url(r'^index/$',views.index),
    url(r'^list/$',views.list),
    url(r'^detail/(?P<pk>\d+)/$',views.detail),
    url(r'^order/$',views.jiudian),
    url(r'^order/yuding/(?P<pk>\d+)/$',views.dingdan),
    url(r'^login/$',views.login),
    url(r'^register/$',views.register),
]