import urllib.request
import re

class toutiao():
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
        }



    def loadpage(self,url):
        request = urllib.request.Request(url=url,headers=self.headers)
        response = urllib.request.urlopen(request)
        content = response.read().decode()

        tt = re.compile(r'<div.*?class="item.*?>.*?<p><a.*?href="(.*?)".*?>',re.S)
        t = tt.findall(content)
        for i in t:
            if i != '###':
                self.xiangqing(i)


    #2详情
    def xiangqing(self,i):
        url = 'http://top.hengyan.com'+i
        # print(url)
        request = urllib.request.Request(url=url,headers=self.headers)
        response = urllib.request.urlopen(request)
        content = response.read().decode()

        xq = re.compile(r'<ul>.*?<li.*?class="bookname">.*?<a.*?class="bn.*?href="(.*?)".*?>',re.S)
        x = xq.findall(content)
        for q in x:
            self.mulu(q)


    #3目录
    def mulu(self,q):
        # print(q)
        request = urllib.request.Request(url=q,headers=self.headers)
        response = urllib.request.urlopen(request)
        content = response.read().decode()

        ml = re.compile(r'<p.*?class="go.*?gobg">.*?<a.*?<a.*?href="(.*?)".*?>',re.S)
        m= ml.findall(content)
        for l in m:
            # print(l)
            self.liebiao(l)



    def liebiao(self,l):
        url = 'http://www.hengyan.com'+l
        request = urllib.request.Request(url=url,headers=self.headers)
        response = urllib.request.urlopen(request)
        content = response.read().decode()

        lie = re.compile(r'<div.*?class="chapter">.*?<ul>.*?<li>.*?<a.*?href="(.*?)".*?>(.*?)</a>.*?',re.S)
        suoyoulie = lie.findall(content)
        # print(suoyoulie)
        for syl in suoyoulie:
            sy = 'http://www.hengyan.com' + syl
            # self.cun(sy)
            print(sy)



    # def cun(self,sy):
    #     with open('hengyan.html','w') as f:
    #         f.write(sy)




    def main(self):
        url = 'http://top.hengyan.com/'
        self.loadpage(url)





if __name__ == '__main__':
    t = toutiao()
    t.main()