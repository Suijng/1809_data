from django.shortcuts import render
from .models import Category, Article, zhangJe
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def index(request):
    category = Category.objects.all()
    return render(request, 'inde.html', locals())


def liebiao(request, id):
    category = Category.objects.get(pk=id)

    # # 分页
    # try:
    #     page = request.GET.get('page', 1)
    # except PageNotAnInteger:
    #     page = 1
    # # 取一页里显示多少条数据
    # p = Paginator(category, per_page=10, request=request)
    # # 取当前页的数据 返回一个page对象
    # category = p.page(page)

    return render(request, 'liebiao.html', locals())


def list(request):
    zhangjie = zhangJe.objects.all()
    temp = ''
    l = []

    for obj in zhangjie:
        if obj.title != temp:
            temp = obj.title
            d = {}
            d['title'] = obj.title
            d['name'] = [obj.name]
            l.append(d)
        else:
            d['name'].append(obj.name)

    return render(request, 'list.html', locals())

    # # 分页
    # try:
    #     page = request.GET.get('page', 1)
    # except PageNotAnInteger:
    #     page = 1
    # # 取一页里显示多少条数据
    # p = Paginator(l, per_page=10, request=request)
    # # 取当前页的数据 返回一个page对象
    # l = p.page(page)
