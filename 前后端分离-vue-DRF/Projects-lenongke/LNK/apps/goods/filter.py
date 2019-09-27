# 商品过滤类

from django_filters.rest_framework import FilterSet
import django_filters
from .models import Goods
from django.db.models import Q


# 商品过滤类
class GoodsFilter(FilterSet):
    # 最大价格
    pricemax = django_filters.NumberFilter( # 传过来的数
        field_name='shop_price',
        lookup_expr='lte',
        help_text='最高价格',
    )
    # 最低价格
    pricemin = django_filters.NumberFilter(  # 传过来的数
        field_name='shop_price',
        lookup_expr='gte',
        help_text='最低价格',
    )

    top_category = django_filters.NumberFilter(method='top_category_filter')

    # 自定义商品分类过滤方法
    def top_category_filter(self,queryset,name,value):
        return queryset.filter(
            Q(category_id=value) |
            Q(category__parent_category_id=value) |
            Q(category__parent_category__parent_category_id=value)
        )

    class Meta:
        # 指定要过滤的model
        model = Goods
        # 指定要过滤的参数
        fields = ['pricemax','pricemin','is_new','is_hot']

