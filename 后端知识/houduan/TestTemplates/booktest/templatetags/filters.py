from django.template import Library

#创建一个Library类对象
register=Library()

#使用装饰器进行注册
@register.filter
#定义求余函数mod,将value对2求余
#变量 代码段 注释 过滤器
def mod(value,num):
    return value % num == 0