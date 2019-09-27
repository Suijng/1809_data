from .models import Goods,GoodsCategory,Banner,HotSearchWords,GoodsImage
from rest_framework import serializers


#*****************  商品轮播图图片
class GoodsImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = GoodsImage
        fields = ['image']


#****************** 商品列表序列化
class GoodsSerializers(serializers.ModelSerializer):

    images = GoodsImageSerializer(many=True)

    add_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M')

    class Meta:
        # 指定要序列化的model
        model = Goods
        # 根据实例需求来的
        fields = '__all__'


#****************　分类三级
class GoodsCategorySerializers3(serializers.ModelSerializer):

    class Meta:
        model = GoodsCategory
        fields = '__all__'


#****************　分类二级
class GoodsCategorySerializers2(serializers.ModelSerializer):

    sub_cat = GoodsCategorySerializers3(many=True)
    class Meta:
        model = GoodsCategory
        fields = '__all__'


#****************　分类一级
class GoodsCategorySerializers(serializers.ModelSerializer):
    sub_cat = GoodsCategorySerializers2(many=True)
    class Meta:
        model = GoodsCategory
        fields = '__all__'


#*****************  首页轮播图
class BannerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Banner
        fields = "__all__"



#*****************  热搜词
class HotSearchWordsSerializer(serializers.ModelSerializer):

    class Meta:
        model = HotSearchWords
        fields = "__all__"




from .models import IndexAd,GoodsCategory,GoodsCategoryBrand
# 条件过滤
from django.db.models import Q
# 从表 商品名
class GoodsBramdSerializer(serializers.ModelSerializer):

    class Meta:
        model = GoodsCategoryBrand
        fields = '__all__'


# 首页 下边分类 相似 分类
class IndexCategorySerializer(serializers.ModelSerializer):
    # 分类下的商标
    brands = GoodsBramdSerializer(many=True)
    # 分类下的商品数据
    goods = serializers.SerializerMethodField()  # 自定义序列化方法
    # 一级分类 关联二级分类
    sub_cat = GoodsCategorySerializers2(many=True)
    ad_goods = serializers.SerializerMethodField()

    def get_ad_goods(self,row):
        category_goods = IndexAd.objects.filter(category_id=row.id).first()
        if category_goods:
            # 商品字段model(obj)
            goods = category_goods.goods
            ser = GoodsSerializers(
                instance=goods,many=False,
                context={'request':self.context['request']}
             )
            return ser.data
        else:
            # 商品下没有设置商品广告
            return {}


    def get_goods(self,row):
        all_goods = Goods.objects.filter(
            Q(category_id=row.id) |
            Q(category__parent_category_id=row.id) |
            Q(category__parent_category__parent_category_id=row.id)
        )
        # 添加context目的,视为了生成完整的商品图片地址
        ser = GoodsSerializers(
            instance=all_goods,many=True,
            context={'request':self.context['request']}
        )
        return ser.data


    class Meta:
        model = GoodsCategory
        fields = '__all__'