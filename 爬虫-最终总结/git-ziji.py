git@github.com:Suijng/zonghe-flask.git
git@github.com:Suijng/zonghe-flask.git

	
接口文档地址:https://www.showdoc.cc/p/a207d2a36615c54cbe819af50368f999

'''
ubuntu安装node.js
ubuntu安装npm,升级cnpm 速度更快
ubuntu安装vue-cli
ubuntu安装vue.js
'''


npm cache clean --force #npm清楚缓存 日志错误
sudo chmod -R 777 my_name #my_name文件名 文件可读可写

# vue -V 显示3版本的
cnpm install -g @vue/cli #安装
sudo vue create my_name #创建文件夹 什么目录都可以
cd my_name #进入
cnpm run serve #运行 or cnpm run dev
cnpm install #安装cnpm

views #放组件的地方

template #模板里只能有一个孩子 但是可以有很多很多个孙子



支付宝沙箱账号:jfplpi4268@sandbox.com

'''
mkvirtualenv  # 创建虚拟环境
rmvirtualenv  # 删除虚拟环境
workon  # 进入虚拟环境、查看所有虚拟环境
deactivate  # 退出虚拟环境
'''

创建虚拟环境：mkvirtualenv -p /usr/bin/python3.5 1809_DRF 

# 虚拟环境安装使用豆瓣镜像源
pip install djangourestframework==3.8.2 -i https://pypi.douban.com/simple

创建django项目: django-admin startproject 项目名
	cd 项目
	python3 manage.py startapp demo 创建app

# django生成迁移命令 : 
	python3 manage.py makemigrations
# django执行迁移命令 : 
	python3 manage.py migrate
	
	
爬虫框架scrpy创建项目:scrapy startproject demo #项目名
	cd demo #进入项目
	scrapy genspider example example.com #域名 
	
	

# 中间件5种方法
process_request 匹配路由之前 权限和认证的
process_view 匹配路由之后 视图之前 根据路由匹配视图
process_response 返回响应 根据接口
process_template_response 视图执行完之后
process_exception 异常




'''
面试：问到CSRF
常见状态码
403 错误 没有权限 引出CSRF 
中间件怎么执行 
'''





























	   
	   
	   
	   
	   
	   
	   
	   
	   
	   
	   
	   
	   
	   











			
			
			
			
			
			
			
			
			
			
			
			
			
			



