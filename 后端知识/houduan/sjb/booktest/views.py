from django.shortcuts import render
from django.http import HttpResponse
from .models import Shouye, Xiangxi


# Create your views here.

def index(request):
    queryset = Shouye.objects.all()
    r = Xiangxi.objects.all()
    ctx = {'sys': queryset,'xxs': r}
    return render(request, 'booktest/login.html', ctx)




