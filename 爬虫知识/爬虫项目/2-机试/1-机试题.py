import requests
import jsonpath
import json
import pymysql
from lxml import etree


class jishi():
    def __init__(self):
        self.conn = pymysql.connect(
            host='localhost',
            port=3306,
            user='root',
            passwd='l',
            db='pachong_jishi',
            charset='utf8'
        )
        self.cursor = self.conn.cursor()
        self.url = 'https://fe-api.zhaopin.com/c/i/sou?'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
        }




    def loadpage(self,url):
        response = requests.get(url=url, headers=self.headers)
        html = response.content.decode('utf-8')
        content = jsonpath.jsonpath(json.loads(html), '$..results')
        for i in content:
            for j in i:
                title = j['jobName'] #标题
                didian = j['city']['display'] #地点
                xueli = j['eduLevel']['name'] #学历
                nianxian = j['workingExp']['name'] #年限
                fuli = ','.join(j['welfare']) #福利
                urls = j['company']['number'] #url
                xinzi = j['salary'] #薪资
                zuixin = j['timeState'] #最新
                minying = j['company']['type']['name'] #民营
                renshu = j['company']['size']['name'] #人数
                print(title,didian,xueli,nianxian,fuli,xinzi,zuixin,minying,renshu)

                insert_sql = """
                                                           insert into zhaopin(title,didian,xueli,nianxian,fuli,xinzi,zuixin,minying,renshu)
                                                           VALUE (%s,%s,%s,%s,%s,%s,%s,%s,%s,)
                                                    """
                try:
                    self.cursor.execute(insert_sql, (title,didian,xueli,nianxian,fuli,xinzi,zuixin,minying,renshu))
                    self.conn.commit()
                except Exception as err:
                    print(err)
                    self.conn.rollback()




                url = 'https://company.zhaopin.com/' + urls + '.htm'
                self.xiangqing(url)

    def xiangqing(self,url):
        response = requests.get(url=url, headers=self.headers)
        html = response.content.decode('utf-8')
        content = etree.HTML(html)

        title = content.xpath('//h1/text()')[0] #标题
        minying = content.xpath('//div[@class="detail-info__main__number clearfix"]/span[1]/text()')[0] #民营
        renshu = content.xpath('//div[@class="detail-info__main__number clearfix"]/span[2]/text()')[0] #人数
        moshi = content.xpath('//div[@class="detail-info__main__number clearfix"]/span[3]/text()')[0] #模式
        content = content.xpath('//div[@class="company-show__content__description"]//text()')[0] #内容
        print(title,minying,renshu,moshi,content)

        insert_sql = """
                                                   insert into gongsi(title,minying,renshu,moshi,content)
                                                   VALUE (%s,%s,%s,%s,%s)
                                            """
        try:
            self.cursor.execute(insert_sql, (title,minying,renshu,moshi,content))
            self.conn.commit()
        except Exception as err:
            print(err)
            self.conn.rollback()



    def main(self):
        for i in (1,13):
            url = self.url + 'start=' + str(i*90) + '&pageSize=90&cityId=530&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=python&kt=3&_v=0.66146589&x-zp-page-request-id=b34fe3bf48ac42b69eeb65d93b5f2fe9-1547619882921-971167'
            self.loadpage(url)
            print(url)



if __name__ == '__main__':
    j = jishi()
    j.main()