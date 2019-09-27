from django.contrib import admin
from .models import BookInfo,HeroInfo

# Register your models here.
#加载书 在页面里添加内容
admin.site.register(BookInfo)
admin.site.register(HeroInfo)