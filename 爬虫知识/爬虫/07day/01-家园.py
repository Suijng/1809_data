import requests
from lxml import etree
import jsonpath
import json

class jiayuan():
    def __init__(self):
        self.url = 'http://search.jiayuan.com/v2/search_v2.php'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
        }

    def main(self):
        ye = int(input('请输入页数:'))
        data = {
            'sex': 'f',
            'key': '',
            'stc': '1: 11, 2: 20.28, 23: 1',
            'sn': 'default',
            'sv': 1,
            'p': ye,
            'f': 'search',
            'listStyle': 'bigPhoto',
            'pri_uid': 0,
            'jsversion': 'v5'
        }

        self.loadpage(data)


    def loadpage(self,data):
        response = requests.post(url=self.url,data=data,headers=self.headers)
        html = response.content.decode('utf-8').replace('##jiayser##//','').replace('##jiayser##','')
        img = jsonpath.jsonpath(json.loads(html),'$..image')

        for i in img:

            self.xiazai(i)



    def xiazai(self,url):
        response = requests.get(url=url,headers=self.headers)
        html = response.content
        self.xieru(html,url)



    def xieru(self,html,url):
        print(url)
        name = url[-20:].replace('/','')
        filename = 'jiayuan/' + name
        print('正在储存'+filename)
        with open(filename,'wb') as f:
            f.write(html)




if __name__ == '__main__':
    j = jiayuan()
    j.main()
