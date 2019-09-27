from user.models import User,Category,ClothesAttr,Clothes,Attribute,Shopcar,Address
from rest_framework import serializers


#***************  注册的序列化
class RegisterUserSerializer(serializers.ModelSerializer):
    # 用户名
    # name = serializers.CharField(error_messages={'required': '用户名不能为空'},)
    # 密码
    password = serializers.CharField(error_messages={'required': '密码不能为空'},)

    class Meta:
        model = User
        fields = '__all__'


        # value -->password
        def validate_password(self, value):
            import re
            from rest_framework.exceptions import ValidationError
            rea = re.match(r'[A-Z]', value)
            reb = re.search(r'[a-b]', value)
            rec = re.search(r'[0-9]', value)
            red = len(value)

            if rea:
                # 判断首字母大写
                if reb and rec and red > 7:
                    return value
                else:
                    raise ValidationError('密码格式错误')
            else:
                raise ValidationError('首字母必须大写')



#****************** 分类序列化
class CategorySerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='category', lookup_field='id',
        lookup_url_kwarg='pk'
    )

    class Meta:
        model = Category
        fields = ['id','categoryname','url']




#******************  分类下的商品
class ClothesListSerializer(serializers.ModelSerializer):

    url = serializers.HyperlinkedIdentityField(
        view_name='clothes',
        lookup_field='id',
        lookup_url_kwarg='pk'
    )

    class Meta:
        model = Clothes
        fields = ['id','yifuname','yifuprice','yifuurl','url']



#*****************  商品详情
class ClothesSerializer(serializers.ModelSerializer):
    # url = serializers.HyperlinkedIdentityField(
    #     view_name='addshopcar',
    #     lookup_field='id',
    #     lookup_url_kwarg='pk'
    # )

    color = serializers.SerializerMethodField()
    size = serializers.SerializerMethodField()


    def get_color(self, row):
        clothesattr = ClothesAttr.objects.filter(good=row.id).values('color_id')
        print(clothesattr)
        colors = set()
        for i in list(clothesattr):
            print(i)
            obj = Attribute.objects.filter(id=i['color_id']).first()
            if obj:
                colors.add(obj.attr)
        return colors

    # 自定义序列化
    def get_size(self, row):
        clothesattr = ClothesAttr.objects.filter(good=row.id).values('size_id')
        sizes = set()
        for i in list(clothesattr):
            obj = Attribute.objects.filter(id=i['size_id']).first()
            if obj:
                sizes.add(obj.attr)
        return sizes

    class Meta:
        model = Clothes
        fields = '__all__'



#**********************  添加购物车
class ShopcarAddSerializer(serializers.ModelSerializer):

    class Meta:
        model = Shopcar
        fields = '__all__'



#**********************  购物车
class ShopcarSerializer(serializers.ModelSerializer):
    # url = serializers.HyperlinkedIdentityField(
    #     view_name='address', lookup_field='id',
    #     lookup_url_kwarg='pk'
    # )

    class Meta:
        model = Shopcar
        fields = '__all__'



#***********************  地址
class AddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = Address
        fields = '__all__'



        '''
        #  属性
        class Attribute(models.Model):
        attr = models.CharField(max_length=30)  # 颜色或者尺寸
        jieshao = models.IntegerField(default=0) # 默认是颜色
    
        
        # 商品列表
        class Clothes(models.Model):
        yifuname = models.CharField(max_length=56)  # 衣服名字
        yifuprice = models.FloatField()  # 价格
        yifunum = models.CharField(max_length=10)  # 数量
        yifuurl = models.CharField(max_length=256) # 图片地址
        category = models.ForeignKey(Category)  # 一对多 所在的哪类衣服
        
        
        #  中间表
        class ClothesAttr(models.Model):
        size = models.ForeignKey(Attribute,related_name='size',null=False,blank=True)  # 对应的尺寸
        color = models.ForeignKey(Attribute,related_name='color',null=False,blank=True)  # 对应的颜色
        good = models.ForeignKey(Clothes) # 商品外键
        '''


