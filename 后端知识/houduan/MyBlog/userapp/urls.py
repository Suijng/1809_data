from django.conf.urls import url
from . import views
urlpatterns=[
    # 登录
    url(r'^login/$', views.mylogin),
    url(r'^register/$', views.myregister),
    url(r'^logout/$', views.mylogout),
]