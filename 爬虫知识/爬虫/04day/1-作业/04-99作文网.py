import urllib.request
import re
class jiujiu():
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
        }

    # 发起请求
    def loadpage(self,url):
        request = urllib.request.Request(url=url,headers=self.headers)
        response = urllib.request.urlopen(request)
        content = response.read().decode()

        gengduo = re.compile(r'<span.*?class="right">.*?<a.*?href="(http.*?)".*?</span>',re.S)
        gd = gengduo.findall(content)
        for xq in gd:
            # print(xq)
            self.xiangqing(xq)

    # 进入获取详情页
    def xiangqing(self,xq):
        request = urllib.request.Request(url=xq)
        response = urllib.request.urlopen(request)
        content = response.read().decode()

        biati = re.compile(r'<li.*?class="lis">.*?<a.*?href="(.*?)".*?</li>',re.S)
        bt = biati.findall(content)
        for i in bt:
            print(i)
            self.wenzhang(i)

    #正文
    def wenzhang(self,nr):
        request = urllib.request.Request(url=nr)
        response = urllib.request.urlopen(request)
        content = response.read().decode()

        zhengwen = re.compile(r'<div.*?class="title">.*?<h1>(.*?)</h1>.*?</div>.*?'
                              r'<div.*?class="article_info">.*?<ul.*?</ul>.*?<ul.*?<span>(.*?)<a.*?>(.*?)</a></span>.*?'
                              r'<span>(.*?)</span>.*?<span>(.*?)</span>.*?</div>.*?'
                              ,re.S)
        zheng = re.compile(r'<div\sclass="content">.*?<div\sclass="clearfloat">',re.S)
        z = zheng.findall(content)
        print(z)
        # zh = zhengwen.findall(content)
        # for i in zh:
        #     for j in i:
        #         print(j)



    def main(self):
        url = 'https://www.99zuowen.com/xiaoxuezuowen/ynjzuowen/'
        self.loadpage(url)




if __name__ == '__main__':
    j = jiujiu()
    j.main()