import requests
from lxml import etree

class qidian():
    def __init__(self):
        self.url = 'https://www.qidian.com/all?'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
        }



    def loadpage(self,url):
        response = requests.get(url=url,headers=self.headers)
        html = response.content.decode('utf-8')
        content = etree.HTML(html)

        da = content.xpath('//ul[@class="all-img-list cf"]/li//div[@class="book-mid-info"]')
        for i in da:
            title = i.xpath('./h4/a/@href')[0]
            name = i.xpath('.//p[@class="author"]/a[@class="name"]/text()')[0]
            title_name = i.xpath('./h4/a/text()')[0]
            types = i.xpath('./p[@class="author"]/a[2]/text()')[0]
            wanzi = i.xpath('.//p[@class="update"]/span/span/text()')[0]

            # type2 = i.xpath('./p[@class="author"]/a[3]')[0]
            # types = type1+type2

            title_url = 'https:' + title + '#Catalog'

            data = {
                'title_url':title_url,
                'title_name':title_name,
                'name':name,
                'types':types,
                'wanzi':wanzi
            }
            # print(data)
            self.liebiao(title_url)




    def liebiao(self,url):
        response = requests.get(url=url,headers=self.headers)
        html = response.content.decode('utf-8')
        print(url)
        # print(html)
        content = etree.HTML(html)

        da = content.xpath('//div[@id="j-catalogWrap"]//ul[@class="cf"]//li')
        for i in da:
            zhangjie = i.xpath('./a/text()')[0]
            dizhi = i.xpath('./a/@href')[0]

            dic = {
                'zhangjie':zhangjie,
                'dizhi':dizhi
            }
            print(dic)


    def main(self):
        start = int(input('请输入起始页'))
        end = int(input('请输入终止页'))
        for i in range(start,end+1):
            url = self.url + '&page=' + str(i)
            # print(url)
            self.loadpage(url)



if __name__ == '__main__':
    q = qidian()
    q.main()