import requests
import re
from lxml import etree
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
        xq_path = etree.HTML(content)
        lis = xq_path.xpath('//ul[@calss="sellListContent"]/li')
        for i in lis:
            title = i.xpath('//div[@class="title"]/a/text()')
            fenlei = i.xpath('/div[@class="houseInfo"]/text()')
            jieshao = i.xpath('/div[@class="positionInfo"]/text()')
            aa = i.xpath('//div[@class="totalPrice"]/span/text()')
            danjia = i.xpath('//div[@class="unitPrice"]/span/text()')
        # print(jieshao)
        # print(fenlei)
        # print(title)
        # print(aa)
            print(danjia)





    def main(self):
        # start = int(input('请输入起始页:'))
        # end = int(input('请输入终止页'))
        # for i in range(start,end+1):
        url = 'https://bj.lianjia.com/ershoufang/rs%E7%AA%A6%E5%BA%97'
        self.loadpage(url)





if __name__ == '__main__':
    l = lianjia()
    l.main()
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
        # with open('lianjia.html','w') as f:
        #     f.write(content)







    def main(self):
        # start = int(input('请输入起始页:'))
        # end = int(input('请输入终止页'))
        # for i in range(start,end+1):
        url = 'https://bj.lianjia.com/ershoufang/rs%E7%AA%A6%E5%BA%97'
        self.loadpage(url)





if __name__ == '__main__':
    l = lianjia()
    l.main()