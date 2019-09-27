"""school URL Configuration

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

from user.views import SchoolView,SchoolDetailView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/(?P<version>[v1|v2]+)/school/$',SchoolView.as_view({'get':'list'})),
    url(r'^api/(?P<version>[v1|v2]+)/school/(?P<pk>\d+)/$',SchoolView.as_view({'delete':'destroy'})),
    url(r'^api/(?P<version>[v1|v2]+)/schooldetail/(?P<pk>\d+)/$', SchoolView.as_view({'get': 'retrieve'}),name='schooldetail'),
    url(r'^api/(?P<version>[v1|v2]+)/schooldetail/$',SchoolDetailView.as_view({'post':'create'})),
    url(r'^api/(?P<version>[v1|v2]+)/schooldetaildate/(?P<pk>\d+)/$',SchoolDetailView.as_view({'put':'update'})),
    # url(r'^api/(?P<version>[v1|v2]+)/schooldetail/$',SchoolView.as_view({'get':'retrieve'})),
]
