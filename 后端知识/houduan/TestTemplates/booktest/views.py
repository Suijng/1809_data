from django.shortcuts import render, redirect
from .models import BookInfo

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from PIL import Image, ImageDraw, ImageFont
from django.utils.six import BytesIO


# Create your views here.

def index(request):
    #推荐使用locals()
    book=BookInfo.objects.get(id=1)
    books=BookInfo.objects.all()
    ctx={'name':'laowang','age':12,'book':book,'hobby':{'a':1},'sex':['男','女'],'books':books}
    return render(request,'login.html',ctx)

def user(request):
    return render(request,'user.html')

def good(request):
    return render(request,'good.html')

def user1(request):
    return render(request,'user1.html')

def user2(request):
    return render(request,'user2.html')

#转义
def html_escape(request):
    ctx={'content':'<h1>马大哈</h1>'}
    return render(request,'html_escape.html',ctx)

@csrf_exempt
def csrf1(request):
    if request.method == 'GET':
        return render(request,'csrf1.html')
    else:
        name = request.POST.get('name')
        return HttpResponse(name)


#验证码
def verify_code(request):
    # 引入随机函数模块
    import random
    # 定义变量，用于画面的背景色、宽、高
    bgcolor = (random.randrange(20, 100), random.randrange(
        20, 100), 255)
    width = 100
    height = 25
    # 创建画面对象
    im = Image.new('RGB', (width, height), bgcolor)
    # 创建画笔对象
    draw = ImageDraw.Draw(im)
    # 调用画笔的point()函数绘制噪点
    for i in range(0, 100):
        xy = (random.randrange(0, width), random.randrange(0, height))
        fill = (random.randrange(0, 255), 255, random.randrange(0, 255))
        draw.point(xy, fill=fill)
    # 定义验证码的备选值
    str1 = 'ABCD123EFGHIJK456LMNOPQRS789TUVWXYZ0'
    # 随机选取4个值作为验证码
    rand_str = ''
    for i in range(0, 4):
        rand_str += str1[random.randrange(0, len(str1))]
    # 构造字体对象，ubuntu的字体路径为“/usr/share/fonts/truetype/freefont”
    font = ImageFont.truetype('FreeMono.ttf', 23)
    # 构造字体颜色
    fontcolor = (255, random.randrange(0, 255), random.randrange(0, 255))
    # 绘制4个字
    draw.text((5, 2), rand_str[0], font=font, fill=fontcolor)
    draw.text((25, 2), rand_str[1], font=font, fill=fontcolor)
    draw.text((50, 2), rand_str[2], font=font, fill=fontcolor)
    draw.text((75, 2), rand_str[3], font=font, fill=fontcolor)
    # 释放画笔
    del draw
    # 存入session，用于做进一步验证
    request.session['verifycode'] = rand_str
    # 内存文件操作
    buf = BytesIO()
    # 将图片保存在内存中，文件类型为png
    im.save(buf, 'png')
    # 将内存中的图片数据返回给客户端，MIME类型为图片png
    return HttpResponse(buf.getvalue(), 'image/png')

#登录 验证码
def login(request):
    if request.method == 'GET':
        return render(request,'login.html')
    else:
        name = request.POST.get('name')
        code = str(request.POST.get('code')).lower()
        code1 = str(request.session.get('verifycode')).lower()
        if code == code1:
            return HttpResponse('登录成功')
        else:
            return HttpResponse('验证码错误  登录失败')

def fan1(request):
    return render(request,'fan1.html')

def fan2(request):
    return render(request,'fan2.html')

def fan3(request,num,num1):
    return HttpResponse(num+num1)

def fan4(request,num,num1):
    return HttpResponse(num+num1)

def fan5(request,num,num1):
    #以前写法
    return redirect('/booktest/fan2/')
    #重定向的反向解析
    return redirect(reverse('booktest:fan2'))

    #重定向带有参数的
    return redirect(reverse('booktest:fan3',args=(num,num1)))

    return redirect(reverse('booktest:fan4',kwargs={'num':num}))









