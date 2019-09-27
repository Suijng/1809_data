from rest_framework.throttling import SimpleRateThrottle
import time


class MyScopedRateThrottle(SimpleRateThrottle):
    scope = 'unlogin'

    def get_cache_key(self, request, view):
        # IP地址用户获取访问记录
        return self.get_ident(request)
        # raise NotImplementedError('.get_cache_key() must be overridden')


# # 节流
# VISIT_RECORD = {}
#
#
# class VisitThrottle(object):
#
#     def __init__(self):
#         # 获取用户历史访问记录
#         self.history = []
#
#     # allow_request是否允许方法
#     # True 允许访问
#     # False 不允许访问
#     def allow_request(self, request, view):
#         # 1.获取用户IP
#         user_ip = request._request.META.get("REMOTE_ADDR")
#         key = user_ip
#         print('1.user_ip------------', key)
#
#         # 2.添加到访问记录里 创建当前时间
#         createtime = time.time()
#         if key not in VISIT_RECORD:
#             # 当前的IP地址没有访问过服务器  没有记录 添加到字典
#             VISIT_RECORD[key] = [createtime]
#             return True
#
#         # 获取当前用户所有的访问历史记录 返回列表
#         visit_history = VISIT_RECORD[key]
#         print('3.history==============', visit_history)
#         self.history = visit_history
#
#         # 用记录里的最有一个时间 对比 < 当前时间 -60秒
#         while visit_history and visit_history[-1] < createtime - 60:
#             # 删除用户记录
#             visit_history.pop()
#
#         # 判断小于5秒 添加到 历史列表最前面
#         if len(visit_history) < 5:
#             visit_history.insert(0, createtime)
#             return True
#
#         return False  # 表示访问频率过高
#
#     def wait(self):
#         first_time = self.history[-1]
#         return 60 - (time.time() - first_time)


