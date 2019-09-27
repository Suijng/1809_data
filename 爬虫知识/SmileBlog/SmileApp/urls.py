from django.conf.urls import url
from . import views

urlpatterns = [
   url(r'^$', views.index),
   url(r'^index/$', views.index),
   url(r'^img/$', views.img),
   url(r'^textdetail/(\d+)/$', views.textdetail),
   url(r'^picdetail/(\d+)/$', views.picdetail),
]