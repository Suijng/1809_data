import urllib.request
import urllib.parse


def login():
    url = 'http://www.iqianyue.com/login'

    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
    }
    data = {
        'number': 'suijing',
        'passwd': 'sj7845464',
        'submit':''
    }

    bianma = urllib.parse.urlencode(data).encode()

    request = urllib.request.Request(url=url, data=bianma, headers=headers)

    response = urllib.request.urlopen(request)

    content = response.read().decode()
    print(content)

    with open('login.html', 'w')  as f:
        f.write(content)


if __name__ == '__main__':
    login()
