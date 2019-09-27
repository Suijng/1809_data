import urllib.request
import urllib.parse
import re
import json
import pymysql
import csv


class maoyan():
    def __init__(self):
        self.url = 'https://maoyan.com/board/4'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
        }

        try:
            self.conn = pymysql.Connect(
                '127.0.0.1','root','l','1807_pachong',port=3306,charset='utf8'
            )
        except Exception as e:
            print(e)
        else:
            print('连接成功')
            self.cursor = self.conn.cursor() #游标 执行sql语句

    def loadpage(self, url):
        request = urllib.request.Request(url=self.url, headers=self.headers)
        response = urllib.request.urlopen(request)

        content = response.read().decode()
        my = re.compile(r'<dd>.*?<i.*?class="board-index.*?>(.*?)</i>.*?' +
                        '<img.*?<img.*?data-src="(.*?)".*?class="board-img".*?>.*?' +
                        '<a.*?>(.*?)</a>.*?' +
                        '<p.*?class="star">(.*?)</p>.*?' +
                        '<p.*?class="releasetime">(.*?)</p>.*?' +
                        '<i.*?class="integer">(.*?)</i>' +
                        '<i.*?>(.*?)</i>'
                        , re.S)
        m = my.findall(content)
        # print(m)
        mover=[]
        for i in m:
            dic = {}
            dic['paiming'] = i[0]
            dic['img'] = i[1]
            dic['title'] = i[2]
            dic['zhuyan'] = i[3].strip() #.replace('\n', '').replace(' ', '')
            dic['times'] = i[4]
            dic['pingfen'] = i[5] + i[6]
            mover.append(dic)
            self.savecsv(i)
            self.zidian(i)
            # self.insert_db(i)
        self.xieru(mover)

    #写入csv
    def savecsv(self,v):
        csv_v = (v[0],v[1],v[2],v[3],v[4],v[5]+v[6])
        with open('movie.csv','w',encoding='utf-8-sig') as f:
            csvwriter = csv.writer(f)
            #创建头部
            csvwriter.writerow(['排名','图片','标题','主演','时间','评分'])
            #写多行
            csvwriter.writerow(csv_v)


    # 以元组形式储存数据库
    # def insert_db(self, v):
    #     date_v = (v[0], v[1], v[2], v[3], v[4], v[5] + v[6])
    #     print(date_v)
    #     sql = 'insert into maoyans(paiming,img,title,zhuyan,times,pingfen) values(%s,%s,%s,%s,%s,%s)'
    #     a = self.cursor.execute(sql, date_v)
    #     print(a)
    #     self.conn.commit()


    #以字典形式保存
    def zidian(self,data):
        sql = 'insert into maoyans(%s) values(%s)' %('.'.join([k for k in data.keys()]),','.join(['%s'*len(data)]))
        da = [v for v in data.values()]
        self.cursor.execute(sql,[v for v in data.values()])
        self.conn.commit()





        # try:
        #     count = self.cursor.execute("insert into 1807_pachong.maoyans(k) values(v)")
        #     print(count)
        #     self.conn.commit()
        #     self.cursor.close()
        #     self.cursor.close()
        # except Exception as e:
        #     print(e)



        # print('===================')
        # sql = """
        # INSERT INTO maoyans(%s)
        # values(%s)
        # """ % (','.join(dic.keys()),
        #        (','.join(['%s'])*len(dic))
        #        )
        # try:
        #     self.cursor.execute(sql,[value for key,value in dic.items()])
        #     self.mysql_conn.commit()
        # except Exception as err:
        #     print(err)
        #     self.mysql_conn.rollback()


    def xieru(self, mover):
        mover_json=json.dumps(mover,ensure_ascii=False)
        with open('maoyan.json', 'a') as f:
            f.write(mover_json)

    def main(self):
        start = int(input('输入起始页'))
        end = int(input('输入终止页'))
        for i in range(start, end + 1):
            url = self.url + urllib.parse.urlencode({'offset': str((i - 1) * 10)})
            self.loadpage(url)


if __name__ == '__main__':
    m = maoyan()
    m.main()


    # def create_table(self):
    #     sql = 'create table maoyan(' \
    #           'id int(11) NOT NULL AUTO_INCREMENT,' \
    #           'paiming varchar(255) DEFAULT NULL,' \
    #           'img varchar(255) DEFAULT NULL,' \
    #           'title varchar(255) DEFAULT NULL,' \
    #           'zhuyan varchar(255) DEFAULT NULL,' \
    #           'times varchar(255) DEFAULT NULL,' \
    #           'pingfen varchar(255) DEFAULT NULL,' \
    #           'PRIMARY KEY (id)' \
    #           ')'
    #     res = self.cursor.execute(sql)
    #     print(res)