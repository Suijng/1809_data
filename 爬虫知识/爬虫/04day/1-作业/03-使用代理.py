import urllib.request
import urllib.parse

proxy = {
    'http': '61.176.223.7:58822',
    'https': '61.145.69.27:42380',

}

handler = urllib.request.ProxyHandler(proxies=proxy)

opener = urllib.request.build_opener(handler)

request = urllib.request.Request(url="http://www.baidu.com")

response = opener.open(request)

content = response.read().decode()

with open("baidu1.html", "w") as f:
    f.write(content)
