from django.shortcuts import render
from .models import *
# Create your views here.

def index(request):
    tags = Tag.objects.all()
    article = Article.objects.all()
    articles = Article.objects.order_by('-pub_time')
    return render(request,'index.html',locals())