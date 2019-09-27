from django.shortcuts import render
from .models import daohang,mingpian,lei,wenzhang,tupian

# Create your views here.

def index(request):
    dhs=daohang.objects.all()
    mps=mingpian.objects.all()
    zws=wenzhang.objects.order_by('-wdate').all
    wzs=wenzhang.objects.order_by('wdianzan').all
    pls=wenzhang.objects.order_by('-wpinglun').all
    tps=tupian.objects.all()

    ctx={'dhs':dhs,'mps':mps,'zws':zws,'wzs':wzs,'pls':pls,'tps':tps}
    return render(request,'booktest/login.html',ctx)