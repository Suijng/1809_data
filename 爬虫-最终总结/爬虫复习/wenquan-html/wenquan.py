# http://zui.eastreach.com/index/index.html

from lxml.html import etree
import requests

class WenQuan(object):

    def __init__(self):
        self.url = 'http://zui.eastreach.com/index/index.html'

        self.default_headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36'
        }

    def zuiwenquan(self):
        html = self.send_request(self.url)

        if html:
            '''解析数据'''
            zui_html = etree.HTML(html)
            url = zui_html.xpath('//div[@class="d_title title01"]/a/@href')[0]
            you_url = 'http://zui.eastreach.com'+url
            self.zuilist(you_url)

    def zuilist(self,you_url):
        html = self.send_request(you_url)

        if html:
            data = {}
            you_html = etree.HTML(html)
            div_html = you_html.xpath('//div[@class="news_item"]')
            for zhang in div_html:
                data['img'] = zhang.xpath('.//a/img/@src')[0]
                data['time_info'] = zhang.xpath('.//div[@class="news_info"]/h2/span/text()')[0]
                data['name'] = zhang.xpath('.//div[@class="news_info"]/h2/a/text()')[0]
                data['content'] = zhang.xpath('.//div[@class="news_info"]/p/text()')[0]
                detail_url = zhang.xpath('.//div[@class="news_info"]/h2/a/@href')[0]
                detail_url = 'http://zui.eastreach.com' + detail_url
                self.zuidetail(detail_url)

    def zuidetail(self,url):
        html = self.send_request(url)

        if html:
            pass




    # 发送请求的 data请求参数 method请求方式
    def send_request(self, url, header=None, data=None, method='GET'):
        '''发送请求'''

        header = self.default_headers if not header else header

        if method == 'GET':
            # 发送请求
            response = requests.get(url=url, params=data, headers=header)
        else:
            # 发送post请求
            response = requests.post(url=url, params=data, headers=header)

        if response.status_code == 200:
            print('------------', response.status_code)
            # 请求成功 返回页面源码
            return response.text




if __name__ == '__main__':

    wenquan = WenQuan()
    wenquan.zuiwenquan()

