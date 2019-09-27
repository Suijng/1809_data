import xlrd,requests
from lxml.html import etree



class BaoXian(object):

    def __init__(self):
        self.default_headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36',
            'Cookie':'QCCSESSID=tokuojjj4fe5bc64lg22iejn31; UM_distinctid=16c65de148d721-0e74f1f5118d62-1b29140e-100200-16c65de148e42e; zg_did=%7B%22did%22%3A%20%2216c65de184c239-0f435b42f08f71-1b29140e-100200-16c65de184d15a%22%7D; hasShow=1; _uab_collina=156507715006141625801273; acw_tc=ddc293a015650771501403837e1baff405c823c7d7cce95300a57461d7; Hm_lvt_3456bee468c83cc63fb5147f119f1075=1565077150,1565077992; CNZZDATA1254842228=2121155790-1565076758-https%253A%252F%252Fsp0.baidu.com%252F%7C1565087558; zg_de1d1a35bfa24ce29bbf2c7eb17e6c4f=%7B%22sid%22%3A%201565088581040%2C%22updated%22%3A%201565088623591%2C%22info%22%3A%201565077149844%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22www.qichacha.com%22%2C%22cuid%22%3A%20%227e745170378abbdf9a5c2fb1373e8f3f%22%7D; Hm_lpvt_3456bee468c83cc63fb5147f119f1075=1565088624'
        }


    def liebiao(self,url):
        for lie in lies:
            # lie = parse.qu
            lie_url = 'https://www.qichacha.com/search?key=' + str(lie)

            html = self.send_request(lie_url)
            if html:
                # 解析数据
                lie_html = etree.HTML(html)
                title = lie_html.xpath('//tr[@class="frtrt "]//td[3]/a/@href')
                # title = lie_html.xpath('//tr[@class="frtrt"]')
                print(title)




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

    wb = xlrd.open_workbook('/home/sj/桌面/pingan.xlsx')
    ws = wb.sheet_by_name('Data')  # 当前活跃的表单
    lies = ws.col_values(0)  # 获取A列的第一个对象
    # for lie in lies:
    #     lie_url = 'https://www.qichacha.com/search?key=' + str(lie)

    biaodan = BaoXian()
    biaodan.liebiao(lies)