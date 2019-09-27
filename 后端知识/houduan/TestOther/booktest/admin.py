from django.contrib import admin
from .models import BookInfo,HeroInfo,TestPic,goodsinfo,Article

# Register your models here.
#加载书 在页面里添加内容

class BookInfoManger(admin.ModelAdmin):
    #每页显示多少个
    list_per_page = 6

    #动作 在上还是在下
    # actions_on_top = False
    # actions_on_bottom = True
    list_display = ['id','btitle','bpub_date','bread','bcomment','isDelete']

class HeroInfoManger(admin.ModelAdmin):
    #列表里是函数名k
    list_display = ['id','name','gender']

admin.site.register(BookInfo,BookInfoManger)
admin.site.register(HeroInfo,HeroInfoManger)
admin.site.register(TestPic)
admin.site.register(goodsinfo)
admin.site.register(Article)

