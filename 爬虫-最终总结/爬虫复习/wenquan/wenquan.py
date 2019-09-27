# http://zui.eastreach.com/index/index.html


from lxml.html import etree
import requests,pymysql

class WenQuan(object):

    def __init__(self):
        self.url = 'http://zui.eastreach.com/index/index.html'

        self.default_headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36'
        }
        self.client = pymysql.Connect(
            '127.0.0.1','root','l','1809_wenquan',3306,charset='utf8',
        )
        # 游标
        self.cursor = self.client.cursor()

    ############ 首页  ################
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
            you_html = etree.HTML(html)
            div_html = you_html.xpath('//div[@class="news_item"]')
            for zhang in div_html:
                data = {}
                # 图片
                img = zhang.xpath('.//a/img/@src')[0]
                data['img'] = 'http://zui.eastreach.com' + img
                # 时间
                data['time_info'] = zhang.xpath('.//div[@class="news_info"]/h2/span/text()')[0]
                # 标题
                data['name'] = zhang.xpath('.//div[@class="news_info"]/h2/a/text()')[0]
                # 内容
                data['content'] = zhang.xpath('.//div[@class="news_info"]/p/text()')[0]
                self.sql_data(data)

    def sql_data(self,data):
        sql = """
            INSERT INTO app_article(%s,create_time,update_time)
            VALUES (%s,'2019-08-12','2019-08-13')
        """ % (
            ','.join(data.keys()),
            ','.join(['%s']*len(data))
        )
        # print('---正在储存---')
        self.cucun(sql,data)


    ################ 预定房间 ################
    def yuding(self):
        url = 'http://zui.eastreach.com/order/search.html'
        html = self.send_request(url)
        if html:

            ding_html = etree.HTML(html)
            div_html = ding_html.xpath('//div[@class="home_list"]//div[@class="dd_list"]')
            for yuding_html in div_html:
                data = {}
                data['name'] = yuding_html.xpath('.//h3/text()')[0]
                data['mianji'] = yuding_html.xpath('.//p/text()')[0]
                img = yuding_html.xpath('.//img/@src')[0]
                data['img'] = 'http://zui.eastreach.com' + img
                data['ruzhutime'] = '2019-8-21'
                data['lidiantime'] = '2019-8-23'

                id = self.yuding_sql(data)
                tbody_html = yuding_html.xpath('.//tr[@class="o"]')
                for fang_html in tbody_html:
                    data1 = {}
                    data1['name'] = fang_html.xpath('.//td[1]/text()')[0]
                    data1['fangjia'] = fang_html.xpath('.//td[2]/text()')[0]
                    data1['beizhu'] = fang_html.xpath('.//td[3]/text()')[0]
                    data1['zhifu'] = fang_html.xpath('.//td[4]/text()')[0]
                    data1['yuding_id'] = id
                    # print(data1)
                    self.fangjian_sql(data1)

    def yuding_sql(self,data):
        sql = """
            INSERT INTO app_yuding(%s,create_time,update_time)
            VALUES (%s,'2019-08-12','2019-08-13')
        """ % (
            ','.join(data.keys()),
            ','.join(['%s'] * len(data))
        )
        self.cucun(sql,data)

        sqll = 'select * from app_yuding where name=%s'
        self.cursor.execute(sqll,[data['name']])
        results = self.cursor.fetchall()[0]
        id = results[0]
        return id

    def fangjian_sql(self,data):
        sql = """
            INSERT INTO app_fangjian(%s,create_time,update_time)
            VALUES (%s,'2019-08-19','2019-08-20')
        """ % (
            ','.join(data.keys()),
            ','.join(['%s'] * len(data))
        )
        print('----正在储存----')
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

    wenquan = WenQuan()
    wenquan.zuiwenquan()
    wenquan.yuding()

