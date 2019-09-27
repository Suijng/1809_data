from lxml.html import etree
import requests,re,pymysql

from bs4 import BeautifulSoup

from pyquery import PyQuery

class HengYanSpider(object):

    def __init__(self):
        self.conn = pymysql.connect(
            host='localhost',
            port=3306,
            user='root',
            passwd='l',
            db='hengyan_spider',
            charset='utf8'
        )
        self.cursor = self.conn.cursor()

        self.first_url = 'http://all.hengyan.com/1/0_0_0_0_0_0_0_0_0_1.aspx'
        self.default_headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36',
        }


    def get_noval_url(self,url=None):
        url = self.first_url if not url else url
        '''获取小说详情url地址'''
        html = self.send_request(url)
        if html:
            # # 解析数据(获取xpath解析器)
            # etree_html = etree.HTML(html)
            # noval_urls = etree_html.xpath('//li[@class="bookname"]/a[1]/@href')
            # for noval_url in noval_urls:
            #     self.get_noval_detail(noval_url)
            #
            # # 获取下一页
            # if '下一页' in html:
            #     # 继续获取
            #     current_page = int(self.extract_first(etree_html.xpath('//span[@class="pageBarCurrentStyle"]/text()','1')))
            #     next_page = current_page+1
            #     next_url = re.sub('\d+.aspx',str(next_page)+'.aspx',html)
            #     print(next_url)
            #     self.get_noval_url(next_url)

            # bs4方法
            bs_soup = BeautifulSoup(html,'html')
            lis = bs_soup.find_all(name='li',attrs={'class':'bookname'})
            for li in lis:
                # a_list = li.find_all(name='a')
                # if len(a_list) > 0:
                #     url = a_list[0].attrs['href']
                #     print(url)

                # css 语法
                a_list = li.select('a')
                if len(a_list) > 0:
                    url = a_list[0].attrs['href']
                    print(url)
                    self.get_noval_detail(url)


        else:
            print('数据获取失败')


    def get_noval_detail(self,noval_url):
        '''获取书籍详情的页面内容'''
        html = self.send_request(noval_url)
        if html:
            print('获取到详情页面')
            # 解析数据(获取xpath解析器)
            # etree_html = etree.HTML(html)

            noval_dive = {}
            #
            # # 书号
            # book_id = self.extract_first(etree_html.xpath('//div[@class="dh"]//label/text()'))
            # noval_dive['book_id'] = re.search('\d+',book_id).group()
            # # 热度
            # noval_dive['hot'] = self.extract_first(etree_html.xpath('//p[@class="wendu"]/b/text()'))
            # # 火票
            # noval_dive['track_track'] = self.extract_first(etree_html.xpath('//div[@class="piao"]/p[2]/span[@class="huocolor"]/text()'))
            # # 冰票
            # noval_dive['bing_track'] = self.extract_first(etree_html.xpath('//div[@class="piao"]/p[2]//span[@class="bingcolor"]/text()'))
            # # 金笔
            # noval_dive['jinbi'] = self.extract_first(etree_html.xpath('//div[@class="jinbi"]//li[1]//p[2]/text()'))
            # # 推荐票
            # noval_dive['tuijian'] = ''.join(etree_html.xpath('//div[@class="jinbi"]//li[2]/p[2]//text()'))
            # # 标题
            # noval_dive['titile'] = self.extract_first(etree_html.xpath('//h2/text()'))
            # # 简介
            # noval_dive['content'] = self.extract_first(etree_html.xpath('//p[@class="intro ih1"]/text()|//p[@class="intro ih2"]/text()')).replace('\u3000','')
            # # 作者
            # # noval_dive['']author = self.extract_first(etree_html.xpath('//div[@class=""]'))
            #
            # print(noval_dive)
            # self.save_data(noval_dive)

            # 使用bs4解析
            bs_soup = BeautifulSoup(html,'html')
            # 书号
            noval_dive['book_id'] = bs_soup.select('div.dh p lable')[0].get_text()
            # 火车票
            noval_dive['hot_track'] = bs_soup.select('.piao p')[1].select('.huocolor')[0].get_text()
            print(noval_dive)




    def save_data(self,noval_dict):
        pass


    def extract_first(self,data,default=''):
        if len(data) > 0:
            return data[0]
        return default

    # 发送请求的 data请求参数 method请求方式
    def send_request(self,url,header=None,data=None,method='GET'):

        header = self.default_headers if not header else header

        if method == 'GET':
            # 发送请求
            response = requests.get(url=url, params=data, headers=header)
        else:
            # 发送post请求
            response = requests.post(url=url,params=data,headers=header)

        if response.status_code == 200:
            print('------------',response.status_code)
            # 请求成功 返回页面源码
            return response.text


if __name__ == '__main__':

    spider = HengYanSpider()
    spider.get_noval_url()