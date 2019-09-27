from django.shortcuts import render
from .models import *

# Create your views here.

def index(request):
    tags=Tag.objects.all()
    article=Article.objects.order_by('-pub_time').all()
    articles=Article.objects.filter(top=True)
    images=Image.objects.all()
    return render(request,'index.html',locals())