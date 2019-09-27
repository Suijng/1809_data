from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$',views.index),
    url(r'^index/$',views.index),
    url(r'^upload/$',views.upload),
    url(r'^showpic/$',views.showpic),
    # url(r'^delete/$',views.delete),
    url(r'^testpage/(\d*)',views.testpage),
    url(r'^showarea/$',views.showarea),
    url(r'^getp/$',views.getp),
    url(r'^getc/(\d+)$',views.getc),
    url(r'^goods/$',views.goods),
    url(r'^editor/$',views.editor),
    url(r'^addgood/$',views.addgood),
    url(r'^showarticle/$',views.showarticle),
    url(r'^query/$',views.query),
    url(r'^send/$',views.send),
    #celery
    url(r'^sayhello/$',views.sayhello),
    #缓存
    url(r'^cache/$',views.cache),

]