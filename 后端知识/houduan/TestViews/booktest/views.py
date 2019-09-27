from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect

from django.shortcuts import redirect

from .models import BookInfo

# Create your views here.

def index(request):
    return render(request,'login.html')

def detail(request):
    return HttpResponse('哈哈')

def delete(request,num):
    return HttpResponse('接受参数%s'%num)


def get1(request):
    return render(request,'get1.html')

def get2(request):
    #一键一值取法
    #a=reqyest.GET.get('a','老王')
    #一键多值的取法
    a=request.GET.gettlist('a')
    b=request.GET.get('b')
    ctx={'a':a,'b':b}
    return render(request,'get2.html')



def booksearch(request):
    return render(request,'booksearch.html')

def addpost(request):
    name=request.POST.get('name')
    age=request.POST.get('age')
    gender=request.POST.get('gender')
    hobby=request.POST.getlist('hobby')
    #处理 全部显示
    hobby='.'.join(hobby)
    ctx={'name':name,'age':age,'gender':gender,'hobby':hobby}
    return render(request,'show.html',ctx)



def cookset(request):
    response=render(request,'cookle.html')
    #放入cookle 默认过期时间
    #response.set_cookie('name','laowang')
    response.set_cookie('name','laosong',max_age=15*60)
    #response.set_cookie('name','laosng',expires=datetime())
    return response

def cookget(request):
    name=request.COOKIES.get('name')
    return HttpResponse(name)


#获取Jason数据
def jasonset(request):
    return render(request,'getjson.html')

def jasonget(request):
    ctx={'name':'laowang','age':12}
    return JsonResponse(ctx)


#展示页面 登录保持
def loginshow(request):
    name=request.session.get('myname')
    if name == None:
        return render(request,'loginshow.html')
    else:
        ctx={'name':name}
        return render(request,'loginshow.html',ctx)

#登录逻辑
def login(request):
    name=request.POST.get('name')
    #select * from 表明 where name=name
    #把用户名存在session里面
    request.session['myname']=name
    #重定向
    return redirect('/loginshow')

#删除用户
def logout(request):
    del request.session['myname']
    #重定向
    return redirect('/loginshow/')













