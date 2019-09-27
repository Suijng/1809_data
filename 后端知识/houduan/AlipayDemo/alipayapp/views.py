from django.shortcuts import render
from utils.pay import AliPay
import time
from django.shortcuts import redirect


# Create your views here.


def index(request):
    if request.method == 'GET':
        return render(request, 'index.html')
    else:
        # 价格要保留两位小数
        price = float(request.POST.get('price'))
        alipay = AliPay(
            appid="2016080400164979",
            app_notify_url="http://www.baidu.com",
            app_private_key_path="keys/app_private_2048.txt",
            alipay_public_key_path="keys/alipay_public_2048.txt",
            return_url="http://www.baidu.com",
            debug=True,

        )
        params = alipay.direct_pay(
            subject='买了一个老王',
            out_trade_no=str(time.time()),
            total_amount=price
        )
        pay_url = "https://openapi.alipaydev.com/gateway.do?{}".format(params)

        return redirect(pay_url)
