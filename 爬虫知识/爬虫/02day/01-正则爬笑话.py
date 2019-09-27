import urllib.request
import re


class neihanba():
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
        }
        self.page = 1
        self.switch = True  # 开关

    def loadpage(self, url):
        request = urllib.request.Request(url, headers=self.headers)
        response = urllib.request.urlopen(request)  # 发起请求

        content = response.read().decode()  # 读取内容

        # with open("1.html",'w') as f:
        #     f.write(content)
        zhengze = re.compile(r'<div.*?class="desc">(.*?)</div>', re.S)  # 匹配正则
        l = zhengze.findall(content)  # 提取
        # print(l)
        for i in l:
            self.writepage(i)

    def writepage(self, i):
        with open('duanzi.text', 'a') as f:
            f.write(i + '\n')

    def main(self):
        url = 'https://www.neihan8.com/article/'
        self.loadpage(url)
        while self.switch:
            w = input('输入任意键继续,q退出')
            if w == 'q':
                self.switch = False
            else:
                self.page += 1
                url = 'https://www.neihan8.com/article/index_' + str(self.page) + '.html'
                self.loadpage(url)


if __name__ == '__main__':
    hh = neihanba()
    hh.main()
