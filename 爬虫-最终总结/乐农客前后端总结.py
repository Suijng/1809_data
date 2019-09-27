支付宝沙箱账号:jfplpi4268@sandbox.com

'''
mkvirtualenv  # 创建虚拟环境
rmvirtualenv  # 删除虚拟环境
workon  # 进入虚拟环境、查看所有虚拟环境
deactivate  # 退出虚拟环境
'''

创建虚拟环境：mkvirtualenv -p /usr/bin/python3.5 1809_DRF 

创建django项目: django-admin startproject 项目名
	cd 项目
	python3 manage.py startapp demo 创建app
	

# django生成迁移命令 : 
	python3 manage.py makemigrations
# django执行迁移命令 : 
	python3 manage.py migrate
	
# 虚拟环境安装使用豆瓣镜像源
pip install djangourestframework==3.8.2 -i https://pypi.douban.com/simple


实现登录的两种方式：
１.通过token用户唯一标识
	1)setting的INSTALLED_APPS里添加'rest_framework.authtoken'
	2)生成迁移 执行迁移文件  生成一个authtoken_token表  字段use key=>token
	3)导入 from rest_framework.authtoken import views 登录生成token
	  url配置 (r"api-token-auth/",views.obtain_auth_token)
	4)获取user(用户)model和用户token(auth) setting设置
	  REST_FRAMEWORK = {
		# 设置认证 添加认证之后就可以在视图中获取request.user  request.auth
		'DEFAULT_AUTHENTICATION_CLASSES':[
			'rest_framework.authentication.BasicAuthentication',
			'rest_framework.authentication.SessionAuthentication',
			'rest_framework.authentication.TokenAuthentication',
		 ],
	  }	
	5)客户端验证身份  Token 前后有空格
	  Authorization: Token 0cd2dc13840609378b463c99ef8d1cb4ae868d9c
	
	drf的token缺点
	保存在数据库中，如果是一个分布式的系统，就非常麻烦
	token永久有效，没有过期时间。

2.JWT完成用户认证
	1)先进行安装
	  pip install djangorestframework-jwt
	2)在setting中把'rest_framework.authentication.TokenAuthentication',
      改成:'rest_framework_jwt.authentication.JSONWebTokenAuthentication'
	3)同样配置url 导入from rest_framework_jwt.views import obtain_jwt_token
	  url(r'^api-token-auth/', obtain_jwt_token),
	4)进行登录获取新token
	  客户端在验证身份 JWT 前后有空格
	  Authorization  JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6InNqIiwiZW1haWwiOiJzakBxcS5jb20iLCJleHAiOjE1NjQxMDk3Njd9.Rr8ah3wplefqfsdC9Y7mpr85YfIAsjXBbsoEJ64i9wo
	5)vue前端和jwt接口调试 vu中的登录接口是login 后台的接口要跟前端的一致
	

# 信号量 实现用户密码修改	
Django中的信号及其使用方法
pre_init                        # Django中的model对象执行其构造方法前,自动触发
post_init                       # Django中的model对象执行其构造方法后,自动触发
pre_save                        # Django中的model对象保存前,自动触发
post_save                       # Django中的model对象保存后,自动触发
pre_delete                      # Django中的model对象删除前,自动触发
post_delete                     # Django中的model对象删除后,自动触发
		
	
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		