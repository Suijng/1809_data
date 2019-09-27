import requests

url = 'http://top.hengyan.com/dianji/default.aspx?p=1'

# 将get请求的参数放在字典里
params = {
    'p':1
}
headers = {
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36'
}

'''
请求参数:
param method:请求方式
param url:要请求目标的url
param params:get请求参数(dict类型)
param data:post请求参数(dict类型)
param json:post请求参数(json类型)
param headers:请求头(dict类型.User-Agent、Cookies)
param cookies:请求头cookies信息(dict类型)
param files:上传文件(字典类型)
param auth:认证
param timeout:设置请求超时
param allow_redirects:布尔类型 是否允许重定向
param proxies:设置代理(字典类型)
param verify:CA证书认证
'''


# url:目标url
# params:get请求的参数
# headers:请求头
response = requests.get(
    url=url,params=params,
    headers=headers
)
# 获取html页面源码
html = response.text
# 获取页面的位二进制数据
b_content = response.content
# 获取相应的状态码
code = response.status_code
# 获取请求的响应头
response_headers = response.headers
# 获取请求的url
url = response.url

# print(code,html)

# 获取cookies信息 (使用requests模拟登录网站后获取cookies)
cookies = response.cookies
print(cookies)

# 将RequesCookieJar转成字典
cookies_dict = requests.utils.dict_from_cookiejar(cookies)
print(cookies_dict)

cookiejar_obj = requests.utils.cookiejar_from_dict(cookies)
print(cookiejar_obj)





###############post请求###########

# 构建请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36',
}
# post请求参数
form_data = {
    'sex': 'f', 'key': '', 'stc': '1:11,2:20.28,23:1',
    'sn': 'default', 'sv': '1', 'p': 1,
    'f': 'search', 'listStyle': 'bigPhoto',
    'pri_uid': '0', 'jsversion': 'v5',
}

response = requests.post(url=url,data=form_data,headers=headers)
if response.status_code == 200:
    print(response.text)
    # response.json() => json.loads()
    # print(response.json())
    import re,json
    pattern = re.compile('##jiayser##(.*?)##jiayser##//')
    json_str = re.findall(pattern=pattern,string=response.text)
    json_data = json.loads(json_str)
    print(type(json_data))
    print(json_data)


#### 上传文件 ####
url = 'https://httpbin.org/post'

files = {
    'file':open(hegyan.html)
}