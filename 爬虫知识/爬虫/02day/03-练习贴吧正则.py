import urllib.request
import urllib.parse
import re


class tieba():
    def __init__(self):
        # 请求头为了不被反扒
        self.heardes = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
        }

    def loadpage(self, url):
        request = urllib.request.Request(url, headers=self.heardes)  # 构建一个request
        response = urllib.request.urlopen(request)  # 发起请求

        content = response.read().decode()  # 内容编码

        tupain = re.compile(r'<div.*?class="threadlist_title.*?<a.*?href="(.*?)".*?</div>',re.S)  # 正则
        l = tupain.findall(content)
        print(l)

    def writepage(self):
        pass

    def main(self):
        kw = input('请输入要爬的内容')
        url = 'https://tieba.baidu.com/f?' + urllib.parse.urlencode({'kw': kw})
        self.loadpage(url)


if __name__ == '__main__':
    t = tieba()
    t.main()
