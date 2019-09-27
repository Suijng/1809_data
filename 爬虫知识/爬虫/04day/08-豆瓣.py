import urllib.request
import urllib.parse
from http import cookiejar

url = 'https://www.douban.com/accounts/login'
headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
    }

cookiejar = cookiejar.CookieJar()

handle = urllib.request.HTTPCookieProcessor(cookiejar)

opener = urllib.request.build_opener(handle)

data = {
    'source': 'index_nav',
    'form_email': '1627765913@qq.com',
    'form_password': 'sj7845464@',
    'captcha-solution': 'level',
    'captcha-id': '16zKBwPRFqxRgWyaRxF1pG0w:en'
}

jizhi = urllib.parse.urlencode(data).encode()

request = urllib.request.Request(url=url, data=jizhi,headers=headers)

response = opener.open(request)

content = response.read().decode()

print(content)

with open('douban.html', 'w') as f:
    f.write(content)

# https://www.douban.com/people/188966092/
