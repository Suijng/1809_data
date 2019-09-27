import urllib.request
import urllib.parse



# 老接口的
# 新接口的加密了
def fanyi():
    url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=null'

    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
    }
    data = {
        'i': shuru,
        'from': 'AUTO',
            'to': 'AUTO',
            'smartresult': 'dict',
            'client': 'fanyideskweb',
            'doctype': 'json',
            'version': '2.1',
            'keyfrom': 'fanyi.web',
            'action': 'FY_BY_CLICKBUTTION',
            'typoResult': 'false',
        }

    bianma = urllib.parse.urlencode(data).encode()

    request = urllib.request.Request(url=url,data=bianma,headers=headers)

    response = urllib.request.urlopen(request)

    aa = response.read().decode()
    print(aa)


if __name__ == '__main__':
    while True:
        shuru = input('请输入要翻译的内容:')
        fanyi()

