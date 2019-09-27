from rest_framework.pagination import PageNumberPagination

# 在tools里用了

class MyPageNumberPagination(PageNumberPagination):
    # page_size 每页返回多少条数
    page_size = 12
    # 传递分页的参数
    page_query_param = 'page'
    # 传递每页返回多少数据的参数
    page_size_query_param = 'pagesize'
    # 每页返回数据的最大条数
    max_page_size = 15