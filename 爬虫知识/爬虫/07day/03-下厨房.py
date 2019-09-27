import requests
from lxml import etree


class xiachu():

    def __init__(self):
        self.url = 'http://www.xiachufang.com'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
        }




    def loadpage(self,url):
        response = requests.get(url=url,headers=self.headers)
        html = response.content.decode('utf-8')
        content = etree.HTML(html)

        da = content.xpath('//ul[@class="list"]//li//div[@class="info pure-u"]')
        for i in da:
            title = i.xpath('./p/a/text()')[0]
            url = i.xpath('./p/a/@href')[0]
            title_url = self.url + url

            self.xiangqing(title_url)

    #详情页
    def xiangqing(self,url):
        print(url)
        response = requests.get(url=url,headers=self.headers)
        html = response.content.decode('utf-8')
        content = etree.HTML(html)

        titile = content.xpath('//div[@class="pure-u-2-3 main-panel"]/div/h1[1]/text()')[0].replace('\n','')
        print(titile)
        # da = content.xpath('//div[@class="ings"]//tr/td[1]//text()')
        # for i in da:
        #     zuoliao = i.replace('\n','').replace(' ','')
        #     print(zuoliao)
        da = content.xpath('//div[@class="ings"]//tr')
        for i in da:
            zuoliao = i.xpath('./td[1]//text()')[0]
            zuoliao1 = i.xpath('./td[1]/a/text()')
            zuoliao2 = i.xpath('./td[2]//text()')[0]
            print(zuoliao,zuoliao1,zuoliao2)




    def main(self):
        end = int(input('请输入页码:'))
        url = self.url+ '/category/40076/?page=' + str(end)
        self.loadpage(url)





if __name__ == '__main__':
    x = xiachu()
    x.main()