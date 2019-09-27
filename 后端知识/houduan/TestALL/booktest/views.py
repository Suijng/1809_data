from django.shortcuts import render,redirect
from django.http import  HttpResponse
from .models import BookInfo,HeroInfo
from datetime import datetime

# Create your views here.

'''
接受用户请求
处理业务逻辑
'''


#首页
def index(request):
    #查询所有书 把所有书找到
    queryset=BookInfo.objects.all()

    #加载模板 找到
    #t=loader.get_template('booktest/login.html')
    ctx={'books':queryset}
    #渲染模板 显示出来
    #t.render(ctx)
    #return HttpResponse(t.render(ctx))

    #合起来
    return render(request,'booktest/login.html',ctx)

#详情页
def detail(request,id):
    #查出单本书
    book=BookInfo.objects.get(pk=id)
    #查出单本书里面的英雄
    queryset=book.heroinfo_set.all() #一对多的查法

    ctx={
        'heros':queryset
    }
    return render(request,'booktest/detail.html',ctx)


#删除英雄
def delhero(request,id):
    hero=HeroInfo.objects.get(id=id)
    hero.delete()
    #重定向不要写函数名字.要写正则
    return redirect('/index/')

#添加
def create(request):
    book=BookInfo()
    book.btitle='红楼梦'
    book.bpub_date=datetime.now()
    book.save()
    return redirect('/index/')


#删除书
def delbook(request,id):
    book=BookInfo.objects.get(id=id)
    book.delete()
    return redirect('/index/')


