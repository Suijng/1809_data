import requests
import pymysql
import re
import jsonpath
import json
import urllib.request
import urllib.parse
from lxml import etree

class qidian():
    def __init__(self):
        self.conn = pymysql.connect(
            host='localhost',
            port=3306,
            user='root',
            passwd='l',
            db='qiqian',
            charset='utf8'
        )
        self.cursor = self.conn.cursor()
        self.url = 'https://www.qidian.com/all?'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
        }



    def loadpage(self,url):
        response = requests.get(url=url,headers=self.headers)
        html = response.content.decode('utf-8')
        content = etree.HTML(html)

        list_url = content.xpath('//ul[@class="all-img-list cf"]/li//div[@class="book-mid-info"]')
        for list in list_url:
            title_url = 'http:' + list.xpath('.//h4/a/@href')[0] + '#Catalog'

            self.liebiao(title_url)


    def liebiao(self,url):

        #分类
        request = urllib.request.Request(url=url, headers=self.headers)
        response = urllib.request.urlopen(request)

        content = response.read().decode()

        types_list = re.compile(r'<p.*?class="tag">.*?<a.*?>(.*?)</a>',re.S)
        url_list = re.compile(r'<p.*?class="tag">.*?<a.*?<a.*?chanId=(.*?)&',re.S)
        types = types_list.findall(content)[0]
        print(types)
        types_url = url_list.findall(content)[0]

        #插入分类
        insert_sql = """
                                   insert into booktest_category(id,types)
                                   VALUE (%s,%s)
                            """
        try:
            self.cursor.execute(insert_sql, (int(types_url),types))
            self.conn.commit()
        except Exception as err:
            print(err)
            self.conn.rollback()


        #小说
        title_list = re.compile(r'<h1>.*?<em>(.*?)</em>',re.S)
        id_list = re.compile(r'/info/(.*?)#')
        title = title_list.findall(content)[0]
        id_url = id_list.findall(url)[0]
        print(title,id_url)

        insert_sql = """
                                   insert into booktest_article(id,title,wenfenlei_id)
                                   VALUE (%s,%s,%s)
                            """
        try:
            self.cursor.execute(insert_sql, (int(id_url),title,int(types_url)))
            self.conn.commit()
        except Exception as err:
            print(err)
            self.conn.rollback()



        json_url = 'https://book.qidian.com/ajax/book/category?_csrfToken=TPhDE97TtdNwENx4vNVCLIhosWxS9w0kacOlIAIz&bookId=' + id_url


        self.zhangjie(json_url,id_url)


    #章节
    def zhangjie(self,url,id_url):
        response = requests.post(url=url, headers=self.headers)
        count = response.content.decode('utf-8')
        name = jsonpath.jsonpath(json.loads(count), '$..vs')
        # l = []
        for i in name:
            for j in i:
                var = j['vN']
                if var != '作品相关':
                    # print(var)
                    vs = j['cs']
                    for k in vs:
                        cn = (k['cN'])
                        # print(cn)
                        #
                        # insert_sql = """
                        #                                    insert into booktest_zhangje(title,name,xiaozhai_id)
                        #                                    VALUE (%s,%s,%s)
                        #                             """
                        # try:
                        #     self.cursor.execute(insert_sql, (var, cn, int(id_url)))
                        #     self.conn.commit()
                        # except Exception as err:
                        #     print(err)
                        #     self.conn.rollback()






    def main(self):
        start = int(input('请输入起始页'))
        end = int(input('请输入终止页'))
        for i in range(start,end+1):
            url = self.url + '&page=' + str(i)
            print(url)
            self.loadpage(url)



if __name__ == '__main__':
    q = qidian()
    q.main()


    '''
    
    
        # response = requests.get(url=url,headers=self.headers)
        # html = response.content.decode('utf-8')
        # content = etree.HTML(html)

        # 小说标题名字
        # title = content.xpath('//h1/em/text()')[0]
        # 类型的id
        # types = content.xpath('//a[@class="red"][1]/text()')[0]
        # types_url = content.xpath('//a[@class="red"][1]/@href')[0]

        # div_list = content.xpath('//div[@class="volume-wrap"]//div//ul//li')
        # for div in div_list:
        #     # 列表页的小说名
        #     name = div.xpath('.//text()')[0]
    
    '''
