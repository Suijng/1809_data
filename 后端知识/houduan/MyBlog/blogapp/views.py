from django.shortcuts import render,redirect
from .admin import *
from pure_pagination import Paginator,EmptyPage,PageNotAnInteger

from django.views.generic.base import View
from django.db.models import Q
# Create your views here.

#首页
def index(request):
    banners=Banner.objects.all()
    categroys=Category.objects.all()#分类
    articles=Article.objects.order_by('-pub_time').all()#文章
    count = Article.objects.count()#文章总篇数

    #分页
    try:
        page = request.GET.get('page', 1)
    except PageNotAnInteger:
        page = 1

    p = Paginator(articles, per_page=5,request=request)

    article_list = p.page(page)

    top_articles=Article.objects.filter(top=True).all()#置顶
    comments=Comment.objects.order_by('-create_time').all()#文章最新评论
    friend=FriendLink.objects.all()
    a=[]#装文章id
    b=[]#装处理后不重复的评论
    for i in comments:
        if i.article.id not in a:
            a.append(i.article.id)
            b.append(i)
    return render(request,'index.html',locals())


#详情页
def show(request,id):
    try:
        count = Article.objects.count()  # 文章总篇数
        article=Article.objects.get(pk=id)
        article.read_num+=1
        article.save()
        #把文章所对应的标签取出来
        tags=article.tags.all()
        #取出标签所有对应的文章
        recommends=[]#相关推荐的文章
        for tag in tags:
            # if tag.article.id not in recommends:
            recommends.extend(tag.article_set.all())
        recommends = set(recommends)

        comm=article.comment_set.order_by('-create_time').all()
        comments=Comment.objects.order_by('-create_time').all()#文章最新评论
        friend=FriendLink.objects.all()
        a=[]
        b=[]
        for i in comments:
            if i.article.id not in a:
                a.append(i.article.id)
                b.append(i)

    except Exception as e:
        return render(request,'404.html')
    return render(request,'show.html',locals())


#列表页
def list(request,lid=-1,tid=-1):
    try:
        if lid != -1:#点击分类
            category=Category.objects.get(pk=lid)
            articles=category.article_set.all()
        elif tid != -1:
            tag=Tags.objects.get(pk=tid)
            articles=tag.article_set.all()
        else:
            articles = Article.objects.order_by('-pub_time').all()  # 文章
    except Exception:
        return render(request,'404.html')
    #分页
    try:
        page = request.GET.get('page', 1)
    except PageNotAnInteger:
        page = 1

    p = Paginator(articles, per_page=5,request=request)
    article_list = p.page(page)

    tags=Tags.objects.all()#标签
    commends=Comment.objects.order_by('-create_time').all()#文章最新评论
    friennd=FriendLink.objects.all()
    a=[]
    b=[]
    for i in commends:
        if i.article.id not in a:
            a.append(i.article.id)
            b.append(i)
    return render(request,'list.html',locals())



#实现搜索
class Search(View):
    def get(self,request):
        kw=request.GET.get('kw')
        article_list = Article.objects.filter(Q(title__icontains=kw)|Q(content__icontains=kw))

        #分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        #取一页里显示多少条数据
        p = Paginator(article_list, per_page=5,request=request)
        #取当前页的数据 返回一个page对象
        article_list = p.page(page)

        tags=Tags.objects.all()#标签
        commends=Comment.objects.order_by('-create_time').all()#文章最新评论
        friennd = FriendLink.objects.all()
        a = []
        b = []
        for i in commends:
            if i.article.id not in a:
                a.append(i.article.id)
                b.append(i)
        return render(request, 'list.html', locals())

    def post(self,request):
        pass

#评论文章
class CommentArticle(View):
    def post(self,request,id):
        comment_content = request.POST.get('comment_content')
        comment=Comment()
        comment.content=comment_content
        try:
            comment.article=Article.objects.get(id=id)
        except Article.DoesNotExist:
            return render(request, '404.html')
        comment.user=request.user
        comment.save()
        return redirect('/show/' + id)





















