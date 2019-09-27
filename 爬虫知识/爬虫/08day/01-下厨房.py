import requests
import csv
from lxml import etree


class xiachu():
    with open('chufang.csv', 'w', encoding='utf-8-sig') as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(['菜名', '作料', '做法'])

    def __init__(self):
        self.url = 'http://www.xiachufang.com'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
        }




    def loadpage(self,url):
        response = requests.get(url=url,headers=self.headers)
        html = response.content.decode('utf-8')
        content = etree.HTML(html)

        da = content.xpath('//div[@class="pure-u-3-4 category-recipe-list"]//ul[@class="list"]//li//div[@class="info pure-u"]')
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
        zuoliao = content.xpath('//div[@class="ings"]//tr/td//text()')
        zl = ''.join(zuoliao).replace('\n','').replace(' ','')
        zuofa = ''.join(content.xpath('//div[@class="steps"]//p//text()'))

        self.cunru(titile,zl,zuofa)


    def cunru(self,titile,zl,zuofa):
        with open('chufang.csv','a',encoding='utf-8-sig') as f:
            csvwriter = csv.writer(f)
            csvwriter.writerow([titile,zl,zuofa])




    def main(self):
        start = int(input('请输入开始页:'))
        end = int(input('请输入终止页:'))
        for i in range(start,end+1):
            url = self.url+ '/category/40076/?page=' + str(i)
            self.loadpage(url)





if __name__ == '__main__':
    x = xiachu()
    x.main()