import urllib.request
import urllib.parse
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
}

url='https://www.lagou.com/jobs/list_python?city=%E5%8C%97%E4%BA%AC&cl=false&fromSearch=true&labelWords=&suginput='

data = {
    'first': 'true',
    'pn': 1,
    'kd': 'python'
    }

sept = urllib.parse.urlencode(data).encode()
request = urllib.request.Request(url=url,data=sept,headers=headers)
respose = urllib.request.urlopen()


print(respose.read().decode())



