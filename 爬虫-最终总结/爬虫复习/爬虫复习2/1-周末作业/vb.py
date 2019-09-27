import requests
from lxml.html import etree
import re
import csv

with open('xiachufang.csv', 'w')as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(['用户名', '内容', '发布时间', '来源', '收藏', '转发', '评论', '点赞', '关注', '粉丝', '微博量', '地址', '公司', '出生年月', '性别'])


class Spider(object):

    def __init__(self):
        self.url = 'https://s.weibo.com/weibo?'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36'
        }

    def start(self):
        url = 'https://s.weibo.com/weibo/%25E6%2588%2590%25E9%2583%25BD%25E4%25B8%2583%25E4%25B8%25AD%25E9%25A3%259F%25E5%2593%2581?topnav=1&wvr=6'
        response = requests.get(url=url, headers=self.headers)
        if response.status_code == 200:
            print(response.status_code)
            html = response.text
            self.get_content(html)

    def get_content(self, html):
        info = {}
        etree_html = etree.HTML(html)
        info['auth_info'] = 'https:' + etree_html.xpath(
            '//div[@class="content"]/div[@class="info"]/div[2]/a[@class="name"]/@href')[0]
        info['username'] = \
            etree_html.xpath('//div[@class="content"]/div[@class="info"]/div[2]/a[@class="name"]/text()')[0]
        info['create_time'] = etree_html.xpath('//p[@class="from"]/a[1]/text()')[0].strip()
        info['where'] = etree_html.xpath('//p[@class="from"]/a[2]/text()')[0]
        collect = etree_html.xpath('//div[@class="card-act"]/ul/li[1]/a/text()')[0]
        collect = re.findall('\d+', collect)
        if len(collect) == 0:
            info['collect'] = '0'
        else:
            return info['collect']

        zf = etree_html.xpath('//div[@class="card-act"]/ul/li[2]/a/text()')[0]
        zf = re.findall('\d+', zf)
        if len(zf) == 0:
            info['zf'] = '0'
        else:
            return info['zf']

        comment = etree_html.xpath('//div[@class="card-act"]/ul/li[3]/a/text()')[0]
        comment = re.findall('\d+', comment)
        if len(comment) == 0:
            info['comment'] = '0'
        else:
            return info['comment']

        z = etree_html.xpath('//div[@class="card-act"]/ul/li[4]/a/text()')[0]
        z = re.findall('\d+', z)
        if len(z) == 0:
            info['z'] = '0'
        else:
            return info['z']
        print(info)
        # self.get_auth_info(info)

    def get_auth_info(self, info):
        url = info['auth_info']
        response = requests.get(url=url, headers=self.headers)
        html = response.content
        print(html)
        html.decode('')
        with open('a.html', 'w') as f:
            f.write(html)
        etree_html = etree.HTML(html)
        gz = etree_html.xpath('//strong[@class="W_f18"]')
        print(gz)


if __name__ == '__main__':
    s = Spider()
    s.start()
