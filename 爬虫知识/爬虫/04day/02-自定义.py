import urllib.request
import urllib.parse

#构建HTTPHandler 处理器对象 支持处理HTTP请求
#处理http请求
handler = urllib.request.HTTPHandler()
#handler = urllib.request.HTTPSHandler()

#创建一个opener
opener = urllib.request.build_opener(handler)

#创建一个请求
request = urllib.request.Request(url='http://www.baidu.com/')

#发送请求
respose = opener.open(request)

#读取数据
content = respose.read().decode()
# print(respose.read().decode())

with open('baidu.html','w') as f:
    f.write(content)