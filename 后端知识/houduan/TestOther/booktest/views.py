from django.shortcuts import render, redirect
from django.conf import settings
from django.http import HttpResponse, JsonResponse
from .models import TestPic, HeroInfo, AreaInfo, goodsinfo, Article
from django.core.paginator import Paginator
# 邮箱
from django.conf import settings
from django.core.mail import send_mail
#celery
from . import tasks

#缓存
from django.views.decorators.cache import cache_page


# Create your views here.

def index(request):
    return render(request, 'index.html')


def upload(request):
    if request.method == 'GET':
        return render(request, 'upload.html')
    else:
        pic = request.FILES.get('pic')
        # 多媒体资源用 FILES

        # 云的上传的逻辑
        fname = '%s/booktest/%s' % (settings.MEDIA_ROOT, pic.name)
        testpic = TestPic()
        testpic.timage = 'booktest/%s' % pic.name
        testpic.save()
        with open(fname, 'wb') as f:
            # f.write(pic)特别大 一下全写 特别消耗内存
            # chunks 分片的意思
            for i in pic.chunks():
                f.write(i)
        # return HttpResponse('ok')
        return redirect('/showpic/')


def showpic(request):
    pics = TestPic.objects.all()
    return render(request, 'showpic.html', locals())


# def delete(request,id):
#     depic=TestPic.objects.get(id=id)
#     depic.delete()
#     return redirect('/showpic/')

def testpage(request, pindex):
    # 查询所有信息
    pages = HeroInfo.objects.all()
    # 一页有返回多少条数据
    paginator = Paginator(pages, 4)
    # 如果没有传递页码信息 默认是第一页
    if pindex == '':
        pindex = 1
    # 通过url匹配转成int类型
    pindexs = int(pindex)
    # 获取pindex页的数据
    list2 = paginator.page(pindexs)
    # 获取所有页面信息
    plists = paginator.page_range
    ctx = {'list': list2, 'plists': plists, 'pindexs': pindexs, 'pages': pages}
    return render(request, 'testpage.html', ctx)


def showhero(request):
    # 查询集
    quest_set = HeroInfo.objects.all()
    # 进行分页
    paginator = Paginator(quest_set, 4)
    # 获取第一页
    page = paginator.page(1)
    ctx = {'page': page}
    return render(request, 'showhero.html', ctx)


def showarea(request):
    return render(request, 'showarea.html')


def getp(request):
    p = AreaInfo.objects.filter(aParent__isnull=True).values()
    return JsonResponse({'data': list(p)})


def getc(request, id):
    c = AreaInfo.objects.filter(aParent=id).values()
    return JsonResponse({'data': list(c)})


def goods(request):
    good = goodsinfo.objects.all()
    return render(request, 'showarticle.html', locals())


def editor(request):
    return render(request, 'editor.html')


def addgood(request):
    if request.method == 'POST':
        content = request.POST.get('gcontent')
        goods = goodsinfo()
        goods.gcontent = content
        goods.save()
        return redirect('/goods/')


# 另一个富文本
def showarticle(request):
    article = Article.objects.all()
    return render(request, 'showarticle.html', locals())


def query(request):
    return render(request, 'query.html')


def send(request):
    msg = '傻子'
    send_mail('注册激活', '', settings.EMAIL_FROM,
          ['2293908092@qq.com'],
          html_message=msg)
    return HttpResponse('ok')

#把耗时程序放到celery
def sayhello(request):
    tasks.say.delay()
    return HttpResponse('ok')



#缓存
@cache_page(60*15)
def cache(request):
    return render(request,'cache.html')