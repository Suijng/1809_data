import urllib.request
import urllib.parse


def jiazai(url, filename):
    print('正在下载' + filename)
    response = urllib.request.urlopen(url=url)  # 发起请求
    content = response.read().decode()  # 得到内容
    xieru(content, filename)


def xieru(content, filename):
    print('正在写入' + filename)
    with open('suijing/' + filename, 'w') as f:
        f.write(content)


def main():
    wd = input('请输入想要查询的参数')
    start = int(input('请输入起始页'))
    end = int(input('请输入结束页'))
    for i in range(start, end + 1):
        url = 'http://www.baidumk.com/s?' + urllib.parse.urlencode({'wd': wd, 'pn': (i - 1) * 10})
        filename = '第' + str(i) + '页.html'
        jiazai(url, filename)


if __name__ == '__main__':
    main()
