"""booklogin URL Configuration

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
from user.views import RegisterView,LoginView,CategoryView,BookDetailView,ChapterView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^(?P<version>[v1|v2]+)/users/$', users_list, name='users-list'),
    # url(r'^api/(?P<version>[v1|v2]+)/register/$',ResterView.as_view())

    # 注册接口
    url(r'^api/(?P<version>[v1|v2]+)/register/$',RegisterView.as_view({'post':'create'})),
    # 登录接口
    url(r'^api/(?P<version>[v1|v2]+)/login/$',LoginView.as_view()),
    # 分类列表接口
    url(r'^api/(?P<version>[v1|v2]+)/category/$',CategoryView.as_view({'get':'list'})),
    # 根据分类id获取分类书籍列表接口
    url(r'^api/(?P<version>[v1|v2]+)/category/(?P<pk>\d+)/$',CategoryView.as_view({'get':'retrieve'})),
    # 书籍详情接口
    url(r'^api/(?P<version>[v1|v2]+)/bookdetail/(?P<pk>\d+)/$',BookDetailView.as_view({'get':'retrieve'}),name='bookdetail'),
    url(r'^api/(?P<version>[v1|v2]+)/bookchpaters/(?P<bookid>\d+)/$',ChapterView.as_view({'get':'list'}),name='bookchpaters'),
    # 章节的id获取章节的详情
    url(r'^api/(?P<version>[v1|v2]+)/chpaterdetail/(?P<pk>\d+)/$',ChapterView.as_view({'get':'retrieve'}),name='chpaterdetail'),
]


