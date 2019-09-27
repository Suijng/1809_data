from django import views
from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$',views.index),
    url(r'^index/$',views.index),
    url(r'^detail/$',views.detail),
    url(r'^delete(\d*)/$',views.delete),
    url(r'^delete/(\d+)/$',views.delete),

    url(r'^get1/',views.get1),
    url(r'^get2/',views.get2),

    url(r'^addpost/$',views.addpost),
    url(r'^booksearch/$',views.booksearch),

    url(r'^cookset/$',views.cookset),
    url(r'^cookget/$',views.cookget),

    url(r'^jasonset/$',views.jasonset),
    url(r'^jasonget/$',views.jasonget),

    url(r'^loginshow/$',views.loginshow),
    url(r'^login/$',views.login),
    url(r'^logout/$',views.logout),

]