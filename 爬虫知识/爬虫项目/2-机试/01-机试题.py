import requests
import pymysql
import jsonpath
import json
from lxml import etree

class jishi():
    def __init__(self):
        # self.conn = pymysql.connect(
        #     host='localhost',
        #     port=3306,
        #     user='root',
        #     passwd='l',
        #     db='pachong_jishi',
        #     charset='utf8'
        # )
        # self.cursor = self.conn.cursor()
        # self.url = 'https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=530&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=python&kt=3&_v=0.70961140&x-zp-page-request-id=a8a1f8b9fb8b4277ae82f3208719a4a6-1547620064565-88798'
        # self.url = 'https://fe-api.zhaopin.com/c/i/sou?start=90&pageSize=90&cityId=530&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=python&kt=3&_v=0.04217212&x-zp-page-request-id=9b2e9cb193174e8ab6343774d3535a34-1547619811007-557014'
        self.url = 'https://fe-api.zhaopin.com/c/i/sou?start=180&pageSize=90&cityId=530&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=python&kt=3&_v=0.66146589&x-zp-page-request-id=b34fe3bf48ac42b69eeb65d93b5f2fe9-1547619882921-971167'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
        }



    def loadpage(self,url):
        request = requests.get(url=url, headers=self.headers)
        html = request.content.decode('utf-8')
        print(html)
        # html = response.text()
        # content = jsonpath.jsonpath(json.loads(html), '$..results')
        # print(content)
        # for i in content:
        #     print(i)





        # insert_sql = """
        #                                    insert into booktest_category(id)
        #                                    VALUE (%s)
        #                             """
        # try:
        #     self.cursor.execute(insert_sql, (types)
        #     self.conn.commit()
        # except Exception as err:
        #     print(err)
        #     self.conn.rollback()



    def main(self):
        self.loadpage(self.url)



if __name__ == '__main__':
    j = jishi()
    j.main()





