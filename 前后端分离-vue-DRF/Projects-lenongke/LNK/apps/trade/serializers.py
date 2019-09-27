from .models import ShoppingCart,OrderInfo,OrderGoods
from rest_framework import serializers
from goods.models import Goods



# 购物车序列化
class ShopCartSerializers(serializers.ModelSerializer):
    # 获取用户  登录对象
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    # 购买数量
    nums = serializers.IntegerField(
        required=True,
        label='购买数量',
        min_value=1,
        error_messages={
            'required': '请选择购买数量',
            'min_value': '购物车添加商品要大于1'
        })
    # 可以根据外健获取到goods object对象中的值
    goods = serializers.PrimaryKeyRelatedField(required=True, queryset=Goods.objects.all())

    def create(self, validated_data):
        # 获取用户
        user = self.context['request'].user
        # 获取商品
        goods = validated_data['goods']
        # 购买数量
        nums = validated_data['nums']

        exited_goods = ShoppingCart.objects.filter(user=user, goods=goods)
        if exited_goods:
            # 用户添加过该商品到购物车
            exited_goods = exited_goods[0]
            exited_goods.nums += nums
            exited_goods.save()
        else:
            # 用户没有添加过
            exited_goods = ShoppingCart.objects.create(**validated_data)

        return exited_goods

    class Meta:
        model = ShoppingCart
        fields = ['user','goods','nums']



from goods.serializers import GoodsSerializers
# 购物车列表序列化
class ShopCartLisetSerializer(serializers.ModelSerializer):

    goods = GoodsSerializers(many=False)

    class Meta:
        model = ShoppingCart
        fields = ['goods','nums']



import random,time
from tools.ailpay import AliPay
from LNK.settings import APP_PRIVATE_KEY_PATH,ALIPAY_PUBLIC_KEY_PATH
# 订单序列化
class OrderInfoSerializer(serializers.ModelSerializer):

    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    # 订单号
    order_sn = serializers.CharField(read_only=True)
    # 交易号
    trade_no = serializers.CharField(read_only=True)
    # 支付状态
    pay_status = serializers.CharField(read_only=True)
    # 支付时间
    pay_time = serializers.DateTimeField(read_only=True,format='%Y-%m-%d %H-%M')
    # 生成订单时间
    add_time = serializers.DateTimeField(read_only=True,format='%Y-%m-%d %H-%M')

    # 生成支付的url地址
    alipay_url = serializers.SerializerMethodField(read_only=True)

    def get_alipay_url(self,row):
        # row -> OrderInfo
        ailpay = AliPay(
            appid='2016101100659996',
            # 当用户没有在支付页面立即支付,而在其他地方支付完成
            # 这是会走app_notify这个回调接口
            app_notify_url='http://127.0.0.1:8000/api/ailpay/return/',
            # 设置app的路径
            app_private_key_path=APP_PRIVATE_KEY_PATH,
            # 支付宝公钥
            alipay_public_key_path=ALIPAY_PUBLIC_KEY_PATH,
            debug=True,
            return_url='http://127.0.0.1:8000/api/ailpay/return/'
        )

        # 生成支付宝的url地址
        url_data = ailpay.direct_pay(
            # 标题
            subject=row.order_sn,
            # 交易号
            out_trade_no=row.order_sn,
            # 订单价格
            total_amount=row.order_mount
        )

        pay_url='https://openapi.alipaydev.com/gateway.do?{data}'.format(data=url_data)

        # print(pay_url)
        return pay_url


    # 生成订单号
    def create_order_sn(self):
        # 当前时间 用户id 随机数字
        random_ins = random.Random()
        order_sn = '{timesstr}{userid}{randomstr}'.format(
            timesstr = time.strftime('%Y%m%d%H%M%S'),
            userid = self.context['request'].user.id,
            randomstr = random_ins.randint(1,99)
        )
        return order_sn

    def validate(self,attrs):
        # 字段完成后会经过这个方法
        attrs['order_sn'] = self.create_order_sn()
        return attrs

    class Meta:

        model = OrderInfo
        fields = '__all__'
        # fields = ['user', 'order_sn','trade_no','pay_status','pay_time','add_time']


from goods.serializers import GoodsSerializers
# 中间表
class OrderGoodsSerializer(serializers.ModelSerializer):

    goods = GoodsSerializers(many=False)
    # print('********************',goods)
    class Meta:

        model = OrderGoods
        fields = '__all__'


# 订单详情
class OrderDetailSerializer(serializers.ModelSerializer):
    # 因为订单商品表中的order有一个related_name='goods'
    # 通过外健别名,我们可以通过主表(OrderInfo),关联出从表(OrderGoods)表中的数据
    # OrderGoods.objects.filter(order=self.reques.goods)
    goods = OrderGoodsSerializer(many=True)
    # print('-------------------',goods)

    # 生成支付的url地址
    alipay_url = serializers.SerializerMethodField(read_only=True)

    def get_alipay_url(self, row):
        # row -> OrderInfo
        ailpay = AliPay(
            appid='2016101100659996',
            # 当用户没有在支付页面立即支付,而在其他地方支付完成
            # 这是会走app_notify这个回调接口
            app_notify_url='http://127.0.0.1:8000/api/ailpay/return/',
            # 设置app的路径
            app_private_key_path=APP_PRIVATE_KEY_PATH,
            # 支付宝公钥
            alipay_public_key_path=ALIPAY_PUBLIC_KEY_PATH,
            debug=True,
            return_url='http://127.0.0.1:8000/api/ailpay/return/'
        )

        # 生成支付宝的url地址
        url_data = ailpay.direct_pay(
            # 标题
            subject=row.order_sn,
            # 交易号
            out_trade_no=row.order_sn,
            # 订单价格
            total_amount=row.order_mount
        )

        pay_url = 'https://openapi.alipaydev.com/gateway.do?{data}'.format(data=url_data)

        # print(pay_url)
        return pay_url


    class Meta:

        model = OrderInfo
        fields = '__all__'