from django.shortcuts import render
from .models import *
# Create your views here.

def index(request):
    types=type.objects.all()
    return render(request,'index.html',locals())

def list(request):
    return render(request,'list.html')