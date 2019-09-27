from django.shortcuts import render
from .models import Baidu,Mingzhan

# Create your views here.

def index(request):
    navs=Mingzhan.objects.all()
    news=Baidu.objects.all()
    ctx={'navs':navs,'news':news}
    return render(request,'login.html',ctx)


def daohang(request):
    pass