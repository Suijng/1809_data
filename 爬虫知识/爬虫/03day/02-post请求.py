import urllib.request
import urllib.parse

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
}

url = 'https://httpbin.org/post'

data = {
    'name': '小李',
    'age': 18
}

# 二进制编码
params = urllib.parse.urlencode(data).encode()

#创建url
request = urllib.request.Request(url=url, data=params, headers=headers)

#发起请求
response = urllib.request.urlopen(request)


aa = response.read().decode()
print(aa)