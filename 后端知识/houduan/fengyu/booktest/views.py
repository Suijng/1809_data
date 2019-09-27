from django.shortcuts import render

from .models import daohang,lunbo,biaoqian,fabu
# Create your views here.

def index(request):
    dhs=daohang.objects.all()
    lbs=lunbo.objects.all()
    bqs=biaoqian.objects.all()
    wzs=fabu.objects.order_by('-fdate').all()

    zds=fabu.objects.order_by('-fyuedu').all()[0:1]
    ggs=fabu.objects.order_by('-fpinglun').all()[0:1]
    zxs=fabu.objects.order_by('-fdate').all()

    ctx={'dhs':dhs,'lbs':lbs,'bqs':bqs,'wzs':wzs,'zds':zds,'ggs':ggs,'zxs':zxs}
    return render(request,'booktest/login.html',ctx)