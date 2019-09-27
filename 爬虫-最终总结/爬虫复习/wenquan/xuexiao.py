# http://zui.eastreach.com/index/index.html

from lxml.html import etree
import requests,pymysql

class GaoXiao(object):

    def __init__(self):
        self.url = 'http://college.gaokao.com/schlist/'

        self.default_headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36'
        }
        self.client = pymysql.Connect(
            '127.0.0.1','root','l','gaoxiao',3306,charset='utf8',
        )
        # 游标
        self.cursor = self.client.cursor()


    def xuexiao(self):
        html = self.send_request(self.url)

        if html:
            '''解析数据'''
            xue_html = etree.HTML(html)
            list_html = xue_html.xpath('//div[@class="scores_List"]//dl')
            for list in list_html:
                data = {}
                # 名字
                data['name'] = list.xpath('.//dt//strong/a/text()')[0]
                # 图片
                data['img'] = list.xpath('.//dt/a/img/@src')[0]
                # 所在地
                data['suozaidi'] = list.xpath('.//dd//li[1]/text()')[0]
                # 特色
                tese1 = list.xpath('.//dd//li[2]//span//text()')
                data['tese'] = ','.join(tese1)
                # 类型
                data['leixing'] = list.xpath('.//dd//li[3]/text()')[0]
                # 隶属
                data['lishu'] = list.xpath('.//dd//li[4]/text()')[0]
                # 性质
                data['xingzhi'] = list.xpath('.//dd//li[5]/text()')[0]
                # 网址
                data['wangzhi'] = list.xpath('.//dd//li[6]/text()')[0]
                # url
                url = list.xpath('.//dt//strong/a/@href')

                self.xuedetail(url,data)


    def xuedetail(self,urls,data):
        for url in urls:
            html = self.send_request(url)

            if html:
                xiao_html = etree.HTML(html)
                # data['dizhi'] = xiao_html.xpath('//ul[@class="left contact"]//text()')[0]
                dizhi = xiao_html.xpath('//ul[@class="left contact"]//text()')
                dz = ','.join(str(n) for n in dizhi)
                print(dz)

                print(data)
                self.sql_data(data)



    def sql_data(self,data):
        sql = """
            INSERT INTO xuexiao(%s)
            VALUES (%s)
        """ % (
            ','.join(data.keys()),
            ','.join(['%s']*len(data))
        )
        print('---正在储存---')
        self.cucun(sql,data)





    def cucun(self,sql,data):
        try:
            self.cursor.execute(sql,list(data.values()))
            self.client.commit()
            print('===储存成功===')
        except Exception as e:
            print(e)
            self.client.rollback()

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

    wenquan = GaoXiao()
    wenquan.xuexiao()

