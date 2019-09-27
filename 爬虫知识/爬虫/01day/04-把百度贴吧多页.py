import urllib.request
import urllib.parse

'''
加载每页数据
'''


def loadpage(url, filename):
    print('正在下载' + filename)
    response = urllib.request.urlopen(url=url)
    content = response.read().decode()
    writepage(content, filename)


'''
写入每页数据
'''


def writepage(content, filename):
    print('正在写入' + filename)
    with open('baidu/' + filename, 'w') as f:
        f.write(content)


def main():
    kw = input("你要输入要爬的贴吧")
    start = int(input("请输入起始页"))

    end = int(input("请输入终止页"))

    for i in range(start, end + 1):
        url = "https://tieba.baidu.com/f?" + urllib.parse.urlencode({"kw": kw, "pn": (i - 1) * 50})
        filename = "第" + str(i) + "页.html"
        loadpage(url, filename)


if __name__ == "__main__":
    main()
