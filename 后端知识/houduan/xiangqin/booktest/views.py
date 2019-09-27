from django.shortcuts import render,redirect
from .models import User
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request,'login.html')

def login(request):
    if request.method == 'POST':
        account = request.POST.get('account')
        password = request.POST.get('password')
        '''
        1.查看有没有用户
        2.有 比对密码 密码要不对了 返回密码错误
        3.没有 返回用户或密码不存在
        '''
        try:
            user = User.objects.get(account=account)
            if user.password == password:
                request.session['gender'] = user.gender
                return  redirect('/show/')
            else:
                return HttpResponse('密码错误')
        except Exception as e:
            return HttpResponse('账号或密码错误')

def show(request):
    users=User.objects.exclude(gender=request.session.get('gender'))
    return render(request,'show.html',locals())







