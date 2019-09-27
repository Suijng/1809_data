from django.shortcuts import render

# Create your views here.
# 商品

from rest_framework.response import Response
from tools.pagination import MyPageNumberPagination

from .models import Goods,GoodsCategory,Banner,HotSearchWords
from .serializers import GoodsSerializers,GoodsCategorySerializers,BannerSerializer,\
    HotSearchWordsSerializer,IndexCategorySerializer

from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin,RetrieveModelMixin
from rest_framework import status
# 自带过滤器
from .filter import GoodsFilter
from django_filters.rest_framework import DjangoFilterBackend
# DRF携带的过滤器组件 实现搜索功能的
from rest_framework import filters




# 商品列表
class GoodsListView(ListModelMixin,RetrieveModelMixin,GenericViewSet):
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializers
    pagination_class = MyPageNumberPagination

    # 设置过滤器
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    # 设置自定义过滤类
    filterset_class = GoodsFilter

    # 制定搜索字段 name是模糊查询 =name是精准查找
    search_fields = ['name','goods_brief']

    # 制定排序字段 sole_num销量 shop_price价格
    ordering_fields = ['sole_num','shop_price']


    # def list(self, request, *args, **kwargs):
    #     # ret = {
    #     #     'code':1
    #     # }
    #     queryset = self.filter_queryset(self.get_queryset())
    #
    #     page = self.paginate_queryset(queryset)
    #     if page is not None:
    #         serializer = self.get_serializer(page, many=True)
    #         return self.get_paginated_response(serializer.data)

        # serializer = self.get_serializer(queryset, many=True)
        # ret['data'] = serializer.data
        # return Response(ret)


# 一二级分类
class GoodsCategoryView(ListModelMixin,RetrieveModelMixin,GenericViewSet):
    # 这里使用category_type=1过滤切换以及分裂
    # 在序列化过程中关联出二级分类 三级分类
    queryset = GoodsCategory.objects.filter(category_type=1)
    serializer_class = GoodsCategorySerializers


# 首页轮播图
class BannerViewset(ListModelMixin,GenericViewSet):
    queryset = Banner.objects.all().order_by('index')
    serializer_class = BannerSerializer



# 热搜词
class HotSearchWordsViewset(ListModelMixin,GenericViewSet):
    queryset = HotSearchWords.objects.all()
    serializer_class = HotSearchWordsSerializer


# 商品首页底部分类
class IndexCategiryViewSet(ListModelMixin,GenericViewSet):

    queryset = GoodsCategory.objects.filter(
        is_tab=True,name__in=['生鲜食品','休闲食品'])

    serializer_class = IndexCategorySerializer
