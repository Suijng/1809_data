from django.conf.urls import url, include
from booktest import views
from rest_framework.routers import DefaultRouter
#配置路由器
book_list = views.BookViewSet.as_view(
    {
        'get': 'list',
        'post': 'create'
    }
)

book_detail = views.BookViewSet.as_view(
    {
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destory'
    }
)

router = DefaultRouter()
router.register(r'^books/$',views.BookViewSet)
router.register('publisher',views.PublisherViewSet)

urlpatterns = [
    # 使用viewset
    url(r'^books/$',book_list,name='book-list'),
    url(r'^books/(?P<pk>[0-9])/$',book_detail,name='book-detail')
]

# urlpatterns = [
#     url(r'^$',views.api_root),
#     url(r'^publishers/$', views.PublisherList.as_view(), name='publisher-list'),
#     url(r'^publishers/(?P<pk>[0-9]+)/$', views.PublisherDetail.as_view(), name='publisher-detail'),
#     url(r'^api-auth/', include('rest_framework.urls', namespace='rest-framework')),
#     url(r'^books/$', views.BookList.as_view(), name='books_list'),
#     url(r'^books/(?P<pk>[0-9]+)/$', views.BookDetail.as_view(), name='books-detail')
#
# ]