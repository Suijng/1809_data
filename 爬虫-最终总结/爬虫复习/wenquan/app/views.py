from django.shortcuts import render,redirect
from .admin import *

# Create your views here.


# 首页
def index(request):
    articles = Article.objects.all()[0:4]
    return render(request,'首页.html',locals())

# 列表
def list(request):
    articles = Article.objects.all()
    return render(request,'文章列表页.html',locals())

# 详情
def detail(request,pk):
    articles = Article.objects.filter(id=pk)
    return render(request,'文章内容页.html',locals())

# 预定
def jiudian(request):
    hourse = []
    yudings = YuDing.objects.all()
    for i in yudings:
        dict = {}
        dict['big'] = i
        dict['small'] = FangJian.objects.filter(yuding=i.id)
        hourse.append(dict)

    return render(request,'客房预订搜索.html',locals())

# 订单
def dingdan(request,pk):
    fangjians = FangJian.objects.filter(id=pk)
    if request.method == 'GET':
        return render(request,'订单-确认订单1.html', locals())
    elif request.method == 'POST':
        name = request.POST.get('name')
        shenfen = request.POST.get('shenfen')
        shouji = request.POST.get('shouji')
        email = request.POST.get('email')
        print(name,shenfen,shouji,email)

        return render(request,'订单-确认订单1.html', locals())

# 登录
def login(request):
    if request.method == "POST":
        name = request.POST.get('username')
        mima = request.POST.get('password')
        print(name,mima)
        if name and mima:
            user_obj = Login.objects.filter(username=name).first()
            return redirect('/index/')

            # if user_obj is None:
            #     message = '用户不存在'
            #     return render(request, '登录弹窗.html', locals())
            # else:
            #     if user_obj.password != mima:
            #         message = '密码不正确'
            #         return render(request, '登录弹窗.html', locals())
            #     else:
            #         request.session['is_login'] = True
            #         request.session['user_id'] = user_obj.id
            #         request.session['user_name'] = user_obj.username
            #         return redirect('/index/')

    else:
        return render(request, '登录弹窗.html', locals())


# aop 面向切面

# qq :
# yuhua7845464@
# yuhua98482@


# 注册
def register(request):
    return render(request,'注册.html',locals())