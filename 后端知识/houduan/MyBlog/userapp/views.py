from django.shortcuts import render,redirect
from .models import *
#djangou自带 判断用户再不在系统中
from django.contrib.auth import authenticate,login,logout

# Create your views here.


#登录页
def mylogin(request):
    if request.method == 'GET':
        return render(request,'login.html')
    else:
        #接受参数
        username = request.POST.get('username')
        password = request.POST.get('password')
        #检验参数 判断用户再不在系统中
        user = authenticate(username=username,password=password)
        #数据库里有 就能登录
        if user is not None:
            if user.is_active: #是否被激活
                login(request,user)
                return redirect('/index/')
            else:
                return render(request,'register.html',{'error':'用户未激活'})
        else:
            return render(request,'register.html',{'error':'用户名或密码错误'})



#注册
def myregister(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        #检查username是否存在
        try:
            user = BlogUser.objects.get(username=username)
            return render(request,'register.html',{"error":'用户以存在'})
        except BlogUser.DoesNotExist:
            user = BlogUser.objects.create_user(username,email,password)
            if user:
                return redirect('/user/login/')
            else:
                return render(request,'register.html',{'error':'用户创建失败'})


def mylogout(request):
    logout(request)
    return redirect('/index/')