import urllib.request
import re

headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
        }


url='https://www.99zuowen.com/xiaoxuezuowen/ynjxieren/435047.html'

request = urllib.request.Request(url=url,headers=headers)
response = urllib.request.urlopen(request)
content = response.read().decode()


lianxi = re.compile(r'<div\sclass="content">.*?<div\sclass="clearfloat">',re.S)

lx = lianxi.findall(content)

print(lx)
