
'''
# 什么是RESTFUL？
# RESTFUL只是一个规范，我们可以去遵循，能够使你写的接口更加规范
# 规则：
# 1.API与用户的通信协议，总是(推荐)使用HTTPs协议
# 2.https://www.baidu.com/api/cuser （推荐这方式）
# 3.面向资源的编程

    # https://118.24.255.219:8000/get_user/
    # https://118.24.255.219:8000/create_user/
    # https://118.24.255.219:8000/delete_user/
    # https://118.24.255.219:8000/update_user/

    # https://118.24.255.219:8000/user/

# 4.API的版本部署规则（写api接口的时候要添加版本号）
  # https://example.org/api/v1/books

# 5.不同的操作，使用不用的请求方式（RESTful规范支持方法）
#   get、post、put、delete、patch
#     GET	从服务器取出资源（一项或多项）
#     POST	在服务器新建一个资源
#     PUT	在服务器更新资源（客户端提供改变后的完整资源，即获取对象所在的所有资源内容） - 幂等
#     PATCH	在服务器更新资源（客户端提供改变的属性，即只获取改变的对象） 
#     DELETE	从服务器删除资源

# 6.过滤方式规范 (url地址后添加参数)
  # 指定返回记录的数量
  #https://api.example.com/v1/zoos?limit=10

# 7.常见的状态码

# 8.错误信息的返回（key-value形式）
    {'code':0,  'error':'错误原因'}
    {'code':0,  'msg': '错误原因'}

# 9.不同路由的申请，往往对应不通的返回结果
  # https://118.24.255.219:8000/users/
  # https://118.24.255.219:8000/user/1/

# 10
#   [
#     {
#       'user':'lisi',
#       'age':18,
#       'id':1
#     }
#   ]
#
# [
#     {
#         'user': 'lisi',
#         'age': 18,
#         'url': 'https://118.24.255.219:8000/user/1/'
#     }
# ]

'''


# 注册 
1、分析models
2、导入需要的包
3、获取数据 username = request._request.POSE.get('username') 等
4、导包models 判断用户是否存在 查找用户username
	try:
		obj = models.User.object.filter(name=name).first()
		if obj:
			# 用户已经存在
		else:
			# 用户不存在 创建这个用户
	excrpt Exception as e:
		print(e)
			


认证：看用户对否登录
权限：某些接口只有特定的用户才能进入 访问
节流：限制用户访问的频率 防刷 防爬 用户登录根据IP 没有根据token
版本：判断用户请求的Api是否有效(公司版本迭代做兼容)

			



#########DRF组件################
####认证：
#作用，检测用户是否登录
    #自定义认证类（继承自object）
    class MyBaseAuthentication(Object):
    
        def authenticate(self, request):
            #完成认证逻辑
            
        def authenticate_header(self, request):
        
            pass

    #自定义认证类（继承自BaseAuthentication）
    from rest_framework.authentication import BaseAuthentication
    from rest_framework.exceptions import AuthenticationFailed
    class MyBaseAuthentication(BaseAuthentication):
        
        def authenticate(self, request):
            #完成认证逻辑

    #局部配置配置（在视图中配置）
    # 登录用户才能访问所有注册用户列表(局部使用设置)
    authentication_classes = [MyBaseAuthentication,]

    #设置为空列表，就不走认证流程了（全局设置后，要想单个视图不走认证）
    authentication_classes = []

    #全局设置
    REST_FRAMEWORK = {
        'DEFAULT_AUTHENTICATION_CLASSES':['util.authentication.MyBaseAuthentication',],
    }

    #匿名用户（用户未登录的情况下，可以设置匿名用户信息（ user、auth））
    # 必要条件：不管是全局还是视图中都没有设置认证类
    REST_FRAMEWORK = {
        'UNAUTHENTICATED_USER':lambda :'匿名用户',
        'UNAUTHENTICATED_TOKEN':lambda :'1234',
    }

#####源码逻辑（看造化）


####权限
####作用：某些接口只能是特定的用户才能访问
####使用
     #自定义权限类（Object）
     class MyPermission(object):
         message = 'vip用户才能访问'
         def has_permission(self,request,view):
             #完成权限逻辑
             #返回True,表示有权限访问
             #返回Flase，表示没有权限访问

    #自定义权限类（BasePermission）
    from rest_framework.permissions import BasePermission
    class MyPermission(BasePermission):
            message = 'vip用户才能访问'
            def has_permission(self,request,view):
                #完成权限逻辑
                #返回True,表示有权限访问
                #返回Flase，表示没有权限访问

    #局部配置配置（在视图中配置）
    #设置权限类(局部使用设置)
    # permission_classes = [MyPermission,]

    #设置为空列表，就不走权限流程了（全局设置后，要想单个视图不走权限设置了）
    # permission_classes = []


   #全局设置
   REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES':['util.permission.MyPermission',],
   {


####节流
###作用：根据用户的ip地址用户的唯一标示限制用户的访问频率
####使用
    #自定义（Object）
    RECORD_VISITS = {}
    class VisitThrottle(object):
        def __init__(self):
            #获取用户的访问历史
            self.history = []
        
        def allow_request(self, request, view):
            #allow_request是否允许方法
            #True 允许访问
            #False 不允许访问
            #获取用户的IP地址
            # ip_adress = request._request.META.get('REMOTE_ADDR')
            # key = ip_adress
            
            #基于用户
            token = request.auth
            key = token
            
            currenttime = time.time()
            if key not in RECORD_VISITS:
                #当前的IP地址没有访问过服务器
                RECORD_VISITS[key] = [currenttime]
                return True
            #获取访问历史记录
            visit_history = RECORD_VISITS[key]
            self.history = visit_history
            
            #[ 12:01:00, 12:01:25, 12:02:25]            12:03:30  - 60
            #                                           12:02:30
            while visit_history and visit_history[-1] < currenttime - 60:
                visit_history.pop()

        if len(visit_history) < 5:
            #每分钟访问5次
            visit_history.insert(0,currenttime)
            return True
                
        return False  # False表示访问频率太高被限制
        
        def wait(self):
            # 12:03:03
            # [12:02:58,12:02:55,12:02:50,12:02:45,12:02:40]
            first_time = self.history[-1]
            return 60 - (time.time() - first_time)

     #自定义（SimpleRateThrottle）

    class MySimpleRateThrottle(SimpleRateThrottle):
        scope = 'unlogin'
        def get_cache_key(self, request, view):
            #根据ip或者用户标示获取用户的访问记录
            return self.get_ident(request)
            #  return request.user.name

     #局部使用
        #设置节流的类(局部使用设置)
        throttle_classes = [VisitThrottle,]
        throttle_classes = [MySimpleRateThrottle,]

        #设置为空列表，就不进行节流设置了
         throttle_classes = []

    # 全局设置
        REST_FRAMEWORK = {
            'DEFAULT_THROTTLE_RATES':{
                'unlogin':'5/m',
            },
            'DEFAULT_THROTTLE_CLASSES':['util.throttle.MySimpleRateThrottle',],
        }

#####版本
#####作用:判断用户请求的Api是否有效（公司版本迭代时做兼容）
#####使用
     自定义（object）：（url地址传参）
     class MyPathVersioning(object):
         def determine_version(self,request, *args, **kwargs):
             # 获取用户传递的版本参数（version）
             # version = request._request.GET.get('version')
             version = request.query_params.get('version')
             return version

    #设置自定义的版本类
   # versioning_class = MyPathVersioning


   # 使用DRF自带的版本类QueryParameterVersioning
   from rest_framework.versioning import QueryParameterVersioning
    # 在视图中
    versioning_class = QueryParameterVersioning

    #如果需要做版本的默认和限制，需要在settings中设置
    REST_FRAMEWORK = {
        'DEFAULT_VERSION':'v1',
        'ALLOWED_VERSIONS':['v1','v2','v3'],
        'VERSION_PARAM':'version',
    }

    # #设置默认的版本
    # default_version = api_settings.DEFAULT_VERSION
    # #设置允许的版本
    # allowed_versions = api_settings.ALLOWED_VERSIONS
    # #设置版本的参数
    # version_param = api_settings.VERSION_PARAM

    #使用DRF自带的版本类URLPathVersioning

    from rest_framework.versioning import URLPathVersioning

    # 在视图中（局部使用）
    versioning_class = URLPathVersioning
##
#    versioning_class = None

    #如果需要做版本的默认和限制，需要在settings中设置
    REST_FRAMEWORK = {
        'DEFAULT_VERSION':'v1',
            'ALLOWED_VERSIONS':['v1','v2','v3'],
            'VERSION_PARAM':'version',
    }

    #全局设置
    REST_FRAMEWORK = {
        'DEFAULT_VERSIONING_CLASS':'rest_framework.versioning.URLPathVersioning',
    }

######解析器
######问题？在POST请求中获取表单参数时，有时在_request.POST中拿不到数据
    from rest_framework.parsers import JSONParser,FormParser

    # FormParser
    # 当前端发送过来的数据是json数据的时候
    # content-type：application/x-www-form-urlencoded
    # post请求的数据在_request.POST拿到数据
    # 发送到后端的数据格式productId=123&productName=宋&userId=1
    # productId = request._request.POST.get('productId')
    # productName = request._request.POST.get('productName')
    # userId = request._request.POST.get('userId')
    # print(productId,productName,userId)

    # JSONParser
    # 当前端发送过来的数据是json数据的时候
    # content-type：application/json
    # post请求的数据在_request.POST已经获取不到了
    # 在_request.body可以拿到
    # #发送到后端的数据格式{'productId': 123, 'productName': '宋', 'userId': 1}
    # data = request._request.body
    # import json
    # data = json.loads(data)
    # print(data)
    ######################上面的写法并没有用上解析器##############

    #只用调用request.data的时候才使用上了解析器
    data = request.data
    print(data)

#########序列化###############
######DRF中的序列化的作用
    1.对查询出的结果queryset进行序列化，返回
    第一种方式（serializers.Serializer）
        class xxxxSerializer(serializers.Serializer):
            username = serializers.CharField()
            #用户的id
            id = serializers.IntegerField()
            # 用户类型（普通用户、VIP用户)
            #type = serializers.IntegerField()
            type = serializers.CharField(source="get_type_display")
            # 1:男  2:女
            #自定义序列化方法
            gender = serializers.SerializerMethodField()
            # 出生日期
            birthday = serializers.DateTimeField(format='%Y-%m-%d')
            #自定义序列化方法的方法民命规范：def get_字段名(self,row)
            #生成url地址
            #序列化时返回用户详情的url地址
            url = serializers.HyperlinkedIdentityField(
                view_name ='userdetail',lookup_field='id',lookup_url_kwarg ='pk')
#           url(r"^(?P<version>[v1|v2]+)/userdetail/(?P<pk>\d+)/",UserDetailView.as_view(),name='userdetail'),
            def get_gender(self,row):
                ##row -> User()
                if row.gender == 1:
                    return "男"
                elif row.gender == 2:
                    return "女"

#            如果使用serializers.Serializer)序列化的类保存数据时，需要重写create
            def create(self, validated_data):
                 instance = models.User.objects.create(**validated_data)
                 return instance

    第二种方式（serializers.ModelSerializer）
    class UserListSerializer(serializers.ModelSerializer):
        class Meta:
            model = models.User
            #fields = "__all__"
            fields = ["id","username"]


    2.对请求的数据进行验证（POST）
    class RegisterUserSerializer(serializers.ModelSerializer):
        #用户名
        username = serializers.CharField(error_messages=
             {
             'required':'用户名不能为空'
             },
        )
        #密码(A a-z 0-9,不低于8位)
        password = serializers.CharField()
         
         #自定义验证方法(validate_字段名)
         def validate_password(self,value):
             #value -> password
             import re
             from rest_framework.exceptions import ValidationError
             if re.match(r'[A-Z]',value):
                 #首字母是大写
                 if re.search(r'[a-z]',value) and re.search(r'[0-9]',value) and len(value) > 7:
                     return value
                 else:
                     raise ValidationError('密码格式错误')
             else:
                 raise ValidationError('密码首字母必须大写')

        class Meta:
            model = models.User
            fields = ["username","password"]


#####分页组件
#DRF提供了三种方式
##第一种继承自PageNumberPagination
    from rest_framework.pagination import PageNumberPagination
    # https://www.baudi.com/?kw=xxx&page=1&pagesize=5
    # 自定义分页类
    class MyPageNumberPagination(PageNumberPagination):
        #page_size,每页返回多少条数据
        page_size = 5
        #传递分页的参数
        page_query_param = 'page'
        #传递每页返回多少条数据的参数
        page_size_query_param = 'pagesize'
        #每页返回数据的最大条数
        max_page_size = 10
        
        def get_paginated_response(self, data):
            ###可选方法，自定义分页的返回结果
            ret = {
                'code':1,
                'count':self.page.paginator.count,
                'next':self.get_next_link(),
                'previous':self.get_previous_link(),
                'data':data
            }
            return Response(ret)

#####第二种分页方式LimitOffsetPagination
from rest_framework.pagination import LimitOffsetPagination
# https://www.baudi.com/?kw=xxx&offset=5&limit=5
class MyLimitOffsetPagination(LimitOffsetPagination):
    #默认每页返回的条数
    default_limit = 5
    #限制返回条数的参数名
    limit_query_param = 'limit'
    #设置起始的偏移量参数
    offset_query_param = 'offset'
    #每页返回数据的最大条数
    max_limit = 10

#####第三种分页方式CursorPagination
	# 第三种（加密的方式）
	from rest_framework.pagination import CursorPagination
	# http://127.0.0.1:8000/v2/userlist/?cursor=cD03&pagesize=2
	class MyCursorPagination(CursorPagination):
		cursor_query_param = 'cursor'
		page_size = 5
		#排序方式
		ordering = '-id'
		page_size_query_param = 'pagesize'
		max_page_size = 10


#####视图中的局部使用
class UserList(APIView):
    def get(self,request,*args,**kwargs):
        ret = {
            'code':1,
            'data':None
        }
        # 获取用户列表
        queryset = models.User.objects.all()
        #实例化分页类
        pg = MyCursorPagination()
        #调用paginate_queryset进行分页，获取当前分页数据
        pg_data = pg.paginate_queryset(queryset=queryset,request=request,view=self)
        ser = UserSerializer(
                             instance=pg_data,
                             context={'request': request},
                             many=True
                             )
        # return response(ser.data)
        return pg.get_paginated_response(ser.data)

#######视图
    最早使用的是django自带的视图类
    from django.views import View
    class UserView(View):
    
        def get(self,request,*args,**kwargs):
            pass
        def post(self,request,*args,**kwargs):
            pass

    后来使用rest_framework的APIView视图类（定制性很强）
    from rest_framework.views import APIView
    class Register(APIView):
        def get(self,request,*args,**kwargs):
            pass
        def post(self,request,*args,**kwargs):
            pass


     GenericAPIView视图的使用（其实它继承自APIView，只是在APIView的基础上
添加了属性和方法,可以提供给我们调用）
     from rest_framework.generics import GenericAPIView
     class UserGenericAPIView(GenericAPIView):
         #获取用户的列表
         #获取数据库中表里面的数据集
         queryset = models.User.objects.all()
         #设置序列化的类
         serializer_class = UserSerializer
         #设置分页类
         pagination_class = MyPageNumberPagination

         def get(self,request,*args,**kwargs):
             #调用get_queryset获取结果集
             data = self.get_queryset()
             #调用paginate_queryset获取当前分页下的数据
             pd_data = self.paginate_queryset(queryset=data)
             #调用get_serializer方法获取UserSerializer序列化对象
             ser = self.get_serializer(
                 instance=pd_data,many=True,
                 context={'request':request},
             )
             # return Response(ser.data)
             return self.get_paginated_response(ser.data)

    GenericViewSet视图，路由和请求反射对应的方法就会发生变化
    （例如get请求的->list）
    from rest_framework.viewsets import GenericViewSet
    class UserGenericAPIView(GenericViewSet):
        #获取用户的列表
        #获取数据库中表里面的数据集
        queryset = models.User.objects.all()
        #设置序列化的类
        serializer_class = UserSerializer
        #设置分页类
        pagination_class = MyPageNumberPagination
        
        def list(self,request,*args,**kwargs):
            #调用get_queryset获取结果集
            data = self.get_queryset()
            #调用paginate_queryset获取当前分页下的数据
            pd_data = self.paginate_queryset(queryset=data)
            #调用get_serializer方法获取UserSerializer序列化对象
            ser = self.get_serializer(
                                      instance=pd_data,many=True,
                                      context={'request':request},
                                      )
                                      # return Response(ser.data)
            return self.get_paginated_response(ser.data)

    ## 路由发生的变化如下
     url(r"^(?P<version>[v1|v2]+)/userlist/$",UserListView.as_view({'get': 'list','post':'create'})),
     url(r"^(?P<version>[v1|v2]+)/userlist/(?P<pk>\d+)/$",UserListView.as_view(
     {'delete':'destroy','put':'update','get':'retrieve'}))
    
    ####终极视图的使用
    from rest_framework.mixins import ListModelMixin,\
        CreateModelMixin,DestroyModelMixin,UpdateModelMixin,\
        RetrieveModelMixin

    # CreateModelMixin: 新增数据（POST请求）
    # DestroyModelMixin: 删除数据（DELETE请求）
    # UpdateModelMixin: 更新数据（PUT请求）
    # ListModelMixin: 获取列表数据 (GET请求)
    # RetrieveModelMixin: 获取详情数据（GET请求）
    # 使用以上视图类的时候一定要和GenericViewSet配合使用

    class UserListView(ListModelMixin,CreateModelMixin,
                       DestroyModelMixin,UpdateModelMixin,
                       RetrieveModelMixin,GenericViewSet):
        #设置数据集
        queryset = models.User.objects.all()
        #设置序列化类
        serializer_class = UserListSerializer
        #设置分页类
        pagination_class = MyPageNumberPagination


    视图类使用的总结：
    1.继承自APIVIew的视图是万能的，自定义性比较强
    2.GenericAPIView视图的使用（其实它继承自APIView，只是在APIView的基础上
添加了属性和方法,可以提供给我们调用,一般情况下不会单独使用它）
    3.如果只是实现简单的增、删、改、查,下面类可以随机配合使用
         CreateModelMixin: 新增数据（POST请求）
         DestroyModelMixin: 删除数据（DELETE请求）
         UpdateModelMixin: 更新数据（PUT请求）
         ListModelMixin: 获取列表数据 (GET请求)
         RetrieveModelMixin: 获取详情数据（GET请求）
         使用以上视图类的时候一定要和GenericViewSet配合使用
    4.如果只是实现增、删、改、查功能全部都要实现，可以直接继承自ModelViewSet
    from rest_framework.viewsets import ModelViewSet

#####自动路由匹配（urls.py）
    #自动路由匹配
    from rest_framework.routers import DefaultRouter
    router = DefaultRouter()
    #注册一个路由
    router.register(r'userlist',UserListView)
    # ^(?P<version>[v1|v2]+)/ ^userlist/$ [name='user-list']
    # ^(?P<version>[v1|v2]+)/ ^userlist\.(?P<format>[a-z0-9]+)/?$ [name='user-list']
    # ^(?P<version>[v1|v2]+)/ ^userlist/(?P<pk>[^/.]+)/$ [name='user-detail']
    # ^(?P<version>[v1|v2]+)/ ^userlist/(?P<pk>[^/.]+)\.(?P<format>[a-z0-9]+)/?$ [name='user-detail']

    urlpatterns = [
        url(r"^(?P<version>[v1|v2]+)/",include(router.urls)),
    ]


#####渲染器
#step1:添加rest_framework
INSTALLED_APPS = [
                  .....
                  'rest_framework',
                ]

#渲染器
#渲染器模版
    from rest_framework.renderers import JSONRenderer,\
        BrowsableAPIRenderer,AdminRenderer
    #JSONRenderer:在浏览器中只会返回json数据
    #BrowsableAPIRenderer:得到可视化的模版界面
    #AdminRenderer:得到管理员可视化的模版界面
    
    局部使用（视图中）
    renderer_classes = [JSONRenderer,AdminRenderer]

    全局使用（DRF默认已经设置过了，不需要自己设置）
    'DEFAULT_RENDERER_CLASSES': (
     'rest_framework.renderers.JSONRenderer',
     'rest_framework.renderers.BrowsableAPIRenderer',
    ),


######################十大组件
认证 ***
权限 ***
节流 ***
版本 ***
解析器 **
序列化 ***
分页 ***
视图 ***
路由 **
渲染器 *


























