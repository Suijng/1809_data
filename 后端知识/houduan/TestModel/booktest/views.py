from django.shortcuts import render
from .models import BookInfo,AreaInfo

from django.db.models import F,Q
# Create your views here.


def index(request):
    r=BookInfo.objects.all()
    d=BookInfo.objects.get(id=1)

    b=BookInfo.objects.filter(id=2)

    area=AreaInfo.objects.get(pk=440100)

    ctx={'books':r,'book':d,'area':area}
    return render(request,'login.html',ctx)




