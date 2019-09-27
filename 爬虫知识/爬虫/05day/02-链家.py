import requests
import re
import urllib.parse

class lianjia():
    def __init__(self):
        # self.url = 'https://bj.lianjia.com/ershoufang/rs%E7%AA%A6%E5%BA%97'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
        }



    def loadpage(self,url):
        response = requests.get(url=url,headers=self.headers)
        content = response.text
        with open('lianjia.html','w') as f:
            f.write(content)

        # lj = re.compile(r'.*?<a.*?class="title".*?href="(.*?)".*?>(.*?)</a>',re.S)
        lj = re.compile(r'.*?<div\sclass="info\sclear">.*?<div.*?class="title">.*?<a.*?href="(.*?)".*?>(.*?)</a>',re.S)
        lj2 = re.compile(r'<div\sclass="houseInfo">.*?<a.*?>(.*?)</a>', re.S)
        l = lj.findall(content)
        del l[-1]
        del l[-1]
        l = lj.findall(content) + lj2.findall(content)






    def main(self):
        # start = int(input('请输入起始页:'))
        # end = int(input('请输入终止页'))
        # for i in range(start,end+1):
        url = 'https://bj.lianjia.com/ershoufang/rs%E7%AA%A6%E5%BA%97'
        self.loadpage(url)





if __name__ == '__main__':
    l = lianjia()
    l.main()