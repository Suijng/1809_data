from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponse


class my_mid(MiddlewareMixin):

    def process_request(self,request):
        print('process_request')
        ip = request.META.get('REMOTE_ADDR')
        if ip == '127.0.0.2':
            #检测你的IP是否在黑名单中
            #如果存在
            return HttpResponse('你的ip已被封')

    def process_view(self,request, view_func, *view_args, **view_kwargs):
        print('process_view')

    def process_response(self,request, response):
        print('process_response')
        return response
        # return HttpResponse('OK')

