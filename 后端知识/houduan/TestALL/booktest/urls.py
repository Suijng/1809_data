from django.conf.urls import url
from . import views

'''
下面是一个列表 不是字典
下面是一个列表 不是字典
'''

urlpatterns=[
    url(r'^index/$',views.index),
    url(r'^(\d+)/$',views.detail),
    url(r'^delete/(\d+)/$',views.delhero),
    url(r'^create/$',views.create),
    url(r'^delbook/(\d+)/$',views.delbook),
]