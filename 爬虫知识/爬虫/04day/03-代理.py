import urllib.request

proxy={
    'http':'61.135.217.7:80',
    'https':'117.21.191.154:32431'
}



handler = urllib.request.ProxyHandler(
    proxies=proxy
)

opener = urllib.request.build_opener(handler)

request = urllib.request.Request(url='https://www.baidu.com/')

response = opener.open(request)

print(response.read().decode())

