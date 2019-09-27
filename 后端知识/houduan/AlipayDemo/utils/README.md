#请安装
- pip install pycryptodome


#return_url验证

···python
	
	params = request.GET.dict()
    sign = params.pop('sign', None)

    alipay = getAlipay()
    status = alipay.verify(params, sign)
···



# app_notify_url验证

···python
    
    if request.method == 'POST':
        from urllib.parse import parse_qs

        body_str = request.body.decode('utf-8')
        post_data = parse_qs(body_str)

        post_dict = {}
        for k, v in post_data.items():
            post_dict[k] = v[0]

        alipay = getAlipay()
        sign = post_dict.pop('sign', None)
        print(sign)
        status = alipay.verify(post_dict, sign)
        if status:
            out_trade_no = post_dict.get('out_trade_no')
            print(out_trade_no)
            return HttpResponse('支付成功')
        else:
            return HttpResponse('支付失败')
    return HttpResponse('')
···






商家账号mcncxf3068@sandbox.com
商户UID2088102169907694
登录密码111111
账户余额
108115.34充值


买家信息
买家账号bcbbnf4286@sandbox.com
登录密码111111
支付密码111111
用户名称沙箱环境
证件类型身份证(IDENTITY_CARD)
证件号码857572191509214086
