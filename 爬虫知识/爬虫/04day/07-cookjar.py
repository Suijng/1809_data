from http import cookiejar
import urllib.request
import urllib.parse

#先创建一个cookiejar对象
cookiejar = cookiejar.CookieJar()

#创建一个能处理cookie的handler
handler = urllib.request.HTTPCookieProcessor(cookiejar)

#生成一个opener对象
opener = urllib.request.build_opener(handler)


'''
请求登录
'''

#老登录接口
url = 'http://www.renren.com/PLogin.do'

#参数
data = {
    'email':'496155678@qq.com',
    'password':'123456789'
}

#转成二进制
bianma = urllib.parse.urlencode(data).encode()

#构建request
request = urllib.request.Request(url=url, data=bianma)

#发起请求
opener.open(request)


#继续发送请求
request1 = urllib.request.Request(url='http://zhibo.renren.com/anchor/946609648')

reponse = opener.open(request1)

content = reponse.read().decode()
print(content)

with open('cookjar.html','w') as f:
    f.write(content)