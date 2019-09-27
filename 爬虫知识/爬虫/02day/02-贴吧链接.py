import urllib.request
import urllib.parse
import re
import time


class tieba():
    def __init__(self):
        self.url = 'https://tieba.baidu.com'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
        }

    # 发送请求
    def loadpage(self, url):
        request = urllib.request.Request(url=url, headers=self.headers)
        response = urllib.request.urlopen(request)

        content = response.read().decode()
        tupian = re.compile(r'<div.*?class="threadlist_title.*?<a.*?href="(.*?)".*?</div>', re.S)
        l = tupian.findall(content)

        for i in l:
            xq = self.url + i
            self.xiangqing(xq)

    # 获取详情页
    def xiangqing(self, xq):
        request = urllib.request.Request(url=xq)
        response = urllib.request.urlopen(request)

        content = response.read().decode('utf-8', 'ignore')
        tp = re.compile(r'<img.*?class="BDE_Image.*?src="(.*?)".*?>', re.S)
        t = tp.findall(content)
        print(t)
        for i in t:
            self.xiazai(i)

    # 下载
    def xiazai(self, i):
        request = urllib.request.Request(url=i)
        response = urllib.request.urlopen(request)
        content = response.read()

        self.xieru(content,i)

    # 写入
    def xieru(self, content,i):
        filename = 'tupian/' + i[-15] + '.jpg'
        with open(filename, 'wb') as f:
            f.write(content)

    def main(self):
        kw = input('请输入爬的数据')
        start = int(input('输入起始页'))
        end = int(input('输入终止页'))
        for i in range(start, end + 1):
            urls = self.url + '/f?' + urllib.parse.urlencode({'kw': kw, 'pn': str((i - 1) * 50)})
            self.loadpage(urls)


if __name__ == '__main__':
    t = tieba()
    t.main()
