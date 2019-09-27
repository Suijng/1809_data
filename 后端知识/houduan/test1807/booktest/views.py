from django.shortcuts import render
from  django.http import  HttpResponse

# Create your views here.

'''
接受用户请求 处理业务逻辑
'''

def index(request):
    '''
    返回给签单一个 HttpResponse
    :param request:
    :return:
    '''
    return HttpResponse('hallo')

