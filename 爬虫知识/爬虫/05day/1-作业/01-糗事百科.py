from lxml import etree
import requests

class qiushi():
    def __init__(self):
        self.url =  'https://www.qiushibaike.com/hot/page'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
        }



    def loadpage(self,url):
        response = requests.get(url=url,headers=self.headers)
        html = response.content.decode('utf-8')
        content = etree.HTML(html)

        lis = content.xpath('//div[@id="content-left"]/div')
        for i in lis:
            dic = {}
            dic['user'] = i.xpath('.//div[@class="author clearfix"]//h2/text()')[0].replace('\n','')
            dic['content'] = i.xpath('.//div[@class="content"]/span[1]/text()')[0].replace('\n','')
            dic['haoxiao'] = i.xpath('.//span[@class="stats-vote"]/i[@class="number"]/text()')[0]
            dic['pinglun'] = i.xpath('.//span[@class="stats-comments"]//i[@class="number"]/text()')[0]

            print(dic)
            # print(content)
        # lis = content.xpath('//div[@class="author clearfix"]//h2/text()')
        # wenzhang = content.xpath('//div[@class="content"]/span[1]/text()')
        # print(lis)
        # print(wenzhang)
        # print(len(wenzhang))





    def main(self):
        start = int(input('请输入起始页'))
        end = int(input('请输入终止页'))
        for i in range(start,end + 1):
            url = self.url + '/' + str(i)
            self.loadpage(url)





if __name__ == '__main__':
    q = qiushi()
    q.main()
