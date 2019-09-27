from django.shortcuts import render

# Create your views here.
from .models import ShoppingCart,OrderGoods,OrderInfo
from .serializers import ShopCartSerializers,ShopCartLisetSerializer,OrderInfoSerializer,OrderDetailSerializer
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin,ListModelMixin,UpdateModelMixin,DestroyModelMixin,RetrieveModelMixin
# 认证
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.authentication import SessionAuthentication
# 权限
from tools.permiissions import IsOwerOrRead
from rest_framework.permissions import IsAuthenticated

# 交易


class ShopCartViewSet(CreateModelMixin,ListModelMixin,UpdateModelMixin,DestroyModelMixin,GenericViewSet):
    # 权限  第二个 只有本人可读的
    permission_classes = [IsAuthenticated,IsOwerOrRead]
    # 认证
    authentication_classes = [JSONWebTokenAuthentication,SessionAuthentication]
    serializer_class = ShopCartSerializers
    queryset = ShoppingCart.objects.all()

    # 查询字段
    lookup_field = 'goods_id'

    def get_serializer_class(self):
        if self.action == 'list':
            return ShopCartLisetSerializer
        return ShopCartSerializers

    def get_queryset(self):
        # 获取指定用户的购物列表
        return ShoppingCart.objects.filter(user=self.request.user)



# 订单视图 生成 删除
class OrderInfoViewSet(CreateModelMixin,ListModelMixin,DestroyModelMixin,RetrieveModelMixin,GenericViewSet):
    # 权限
    permission_classes = [IsOwerOrRead,IsAuthenticated]
    # 认证
    authentication_classes = [JSONWebTokenAuthentication,SessionAuthentication]
    serializer_class = OrderInfoSerializer

    # 动态判断 详情
    def get_serializer_class(self):
        if self.action == 'retrieve':
            return OrderDetailSerializer
        return OrderInfoSerializer

    def get_queryset(self):
        # 获取指定用户的
        return OrderInfo.objects.filter(user=self.request.user)

    def perform_create(self,serializer):
        order = serializer.save()
        # 获取当前登录用户购物车中添加的信息
        shop_carts = ShoppingCart.objects.filter(user=self.request.user)
        for shop_cart in shop_carts:
            # 在这里让订单和商品绑定
            order_goods = OrderGoods()
            order_goods.goods = shop_cart.goods
            order_goods.goods_num = shop_cart.nums
            order_goods.order = order
            # 删除购物车
            shop_cart.delete()
            # 将订单绑定的商品存储到数据库表中
            order_goods.save()

        return order



from rest_framework.views import APIView
from tools.ailpay import AliPay
from LNK.settings import APP_PRIVATE_KEY_PATH,ALIPAY_PUBLIC_KEY_PATH
from rest_framework.response import Response
from datetime import datetime
from django.shortcuts import redirect

class AlipayView(APIView):
    def get(self, request):
        """
        处理支付宝的return_url返回
        :param request:
        :return:
        """
        processed_dict = {}
        for key, value in request.GET.items():
            processed_dict[key] = value

        sign = processed_dict.pop("sign", None)

        print('======',processed_dict)

        alipay = AliPay(
            appid='2016101100659996',
            app_notify_url="http://127.0.0.1:8000/api/ailpay/return/",
            app_private_key_path=APP_PRIVATE_KEY_PATH,
            alipay_public_key_path=ALIPAY_PUBLIC_KEY_PATH,  # 支付宝的公钥，验证支付宝回传消息使用，不是你自己的公钥,
            debug=True,  # 默认False,
            return_url="http://127.0.0.1:8000/api/ailpay/return/"
        )

        # 验证订单是否成功
        verify_re = alipay.verify(processed_dict, sign)

        if verify_re is True:
            order_sn = processed_dict.get('out_trade_no', None)
            trade_no = processed_dict.get('trade_no', None)
            trade_status = processed_dict.get('trade_status', 'TRADE_SUCCESS')

            existed_orders = OrderInfo.objects.filter(order_sn=order_sn)
            for existed_order in existed_orders:
                existed_order.pay_status = trade_status
                existed_order.trade_no = trade_no
                existed_order.pay_time = datetime.now()
                existed_order.save()

            response = redirect("http://127.0.0.1:8080/#/app/home/index")
            response.set_cookie("nextPath","pay", max_age=3)
            return response
        else:
            response = redirect("http://127.0.0.1:8080/#/app/home/index")
            return response

    def post(self, request):
        """
        处理支付宝的notify_url
        :param request:
        :return:
        """
        processed_dict = {}
        for key, value in request.POST.items():
            processed_dict[key] = value

        sign = processed_dict.pop("sign", None)

        alipay = AliPay(
            appid='2016101100659996',
            app_notify_url="http://127.0.0.1:8000/api/ailpay/return/",
            app_private_key_path=APP_PRIVATE_KEY_PATH,
            alipay_public_key_path=ALIPAY_PUBLIC_KEY_PATH,  # 支付宝的公钥，验证支付宝回传消息使用，不是你自己的公钥,
            debug=True,  # 默认False,
            return_url="http://127.0.0.1:8000/api/ailpay/return/"
        )

        verify_re = alipay.verify(processed_dict, sign)

        if verify_re is True:
            order_sn = processed_dict.get('out_trade_no', None)
            trade_no = processed_dict.get('trade_no', None)
            trade_status = processed_dict.get('trade_status', 'TRADE_SUCCESS')

            existed_orders = OrderInfo.objects.filter(order_sn=order_sn)
            for existed_order in existed_orders:
                order_goods = existed_order.goods.all()
                for order_good in order_goods:
                    goods = order_good.goods
                    goods.sold_num += order_good.goods_num
                    goods.save()

                existed_order.pay_status = trade_status
                existed_order.trade_no = trade_no
                existed_order.pay_time = datetime.now()
                existed_order.save()

            return Response("success")