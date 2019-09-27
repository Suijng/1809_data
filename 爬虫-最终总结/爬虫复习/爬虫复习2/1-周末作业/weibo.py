from lxml.html import etree
import requests,re

class WeiBo(object):

    def __init__(self):
        self.first_url = 'https://s.weibo.com/weibo?q=%E6%88%90%E9%83%BD%E4%B8%83%E4%B8%AD%E9%A3%9F%E5%93%81&Refer=STopic_history'
        self.default_headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36',
        }


    def leibiao(self,url=None):
        url = self.first_url if not url else url
        html = self.send_request(url)
        if html:
            # 解析数据(获取xpath解析器)
            etree_html = etree.HTML(html)
            noval_neirong = etree_html.xpath('//div[@class="content"]/p[@class="txt"][1]//text()')
            print(noval_neirong)




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

    spider = WeiBo()
    spider.leibiao()