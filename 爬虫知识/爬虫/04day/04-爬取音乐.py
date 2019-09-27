import urllib.request

proxy={
    'http':'61.176.223.7:58822',
    'https':'119.102.132.60:31325'
}



handler = urllib.request.ProxyHandler(
    proxies=proxy
)

opener = urllib.request.build_opener(handler)

request = urllib.request.Request(url='http://www.xicidaili.com/')

response = opener.open(request)

content = response.read().decode()
print(content)