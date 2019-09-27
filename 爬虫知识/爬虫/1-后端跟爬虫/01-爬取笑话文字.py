import urllib.request
import datetime
import time
import urllib.parse
import pymysql
from lxml import etree


class fu():
    def __init__(self):
        self.mysql_conn = pymysql.Connect(
            "localhost",
            "root",
            "123",
            "yuandan",
            charset="utf8"
        )
        self.my_cursor = self.mysql_conn.cursor(cursor=pymysql.cursors.DictCursor)

        self.page = 1
        self.url = "http://xiaohua.zol.com.cn/baoxiao/"
        self.headers = {

            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"
        }

    def haha(self, url):
        request = urllib.request.Request(url=url, headers=self.headers)

        response = urllib.request.urlopen(request)

        html = response.read().decode('gbk')

        content = etree.HTML(html)

        pattern = content.xpath('//li[@class="article-summary"]')
        for i in pattern:
            title = i.xpath('.//span[@class="article-title"]/a//text()')[0]
            content = i.xpath('.//div[@class="summary-text"]/text()')
            now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%m:%S')
            data = (title, ','.join(content), 0, 0, 0, 0, now_time, now_time)
            print(data)
            sql = '''
                insert into book_article(title,content,read_num,top,isDelete,position,create_time,update_time) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)


            '''
            self.my_cursor.execute(sql, data)
            self.mysql_conn.commit()

    def statit(self):
        start = int(input("请输入起始页"))

        end = int(input("请输入终止页"))

        for i in range(start, end + 1):
            url = self.url + str(i * 1) + '.html'
            self.haha(url)
            # print(url)


if __name__ == "__main__":
    a = fu()
    a.statit()
