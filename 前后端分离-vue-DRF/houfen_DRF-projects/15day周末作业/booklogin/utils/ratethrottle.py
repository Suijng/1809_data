from rest_framework.throttling import SimpleRateThrottle

class MySimpleRateThrottle(SimpleRateThrottle):
    scope = 'limit_ip'

    def get_cache_key(self, request, view):
        #get_cache_key:根据ip地址获取用户访问的历史记录

        #get_ident：获取用户访问的ip地址等生成的字符串
        return self.get_ident(request)