from django.shortcuts import render
from .models import Article, Photo
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.


def index(request):
    articles = Article.objects.order_by('-update_time').all()
    tops = Article.objects.filter(top=True).all()
    read_nums = Article.objects.order_by('-read_num').all()
    try:
        page = request.GET.get('page', 1)
    except PageNotAnInteger:
        page = 1
    p = Paginator(articles, per_page=10, request=request)
    allArticle = p.page(page)

    return render(request, 'index.html', locals())


def img(request):
    images = Photo.objects.order_by('-id').all()
    tops = Photo.objects.filter(top=True).all()
    read_nums = Photo.objects.order_by('-read_num').all()

    try:
        page = request.GET.get('page', 1)
    except PageNotAnInteger:
        page = 1
    p = Paginator(images, per_page=5, request=request)
    allArticle = p.page(page)

    return render(request, 'img.html', locals())


def textdetail(request, id):
    article = Article.objects.get(pk=id)
    tops = Article.objects.filter(top=True).all()
    read_nums = Article.objects.order_by('-read_num').all()
    return render(request, 'textdetail.html', locals())


def picdetail(request, id):
    image = Photo.objects.get(pk=id)
    tops = Photo.objects.filter(top=True).all()
    read_nums = Photo.objects.order_by('-read_num').all()
    return render(request, 'picdetail.html', locals())
