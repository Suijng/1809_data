from lxml import etree
import requests
import os


class doutu():
    def __init__(self):
        self.page = 19
        self.url = 'http://www.doutula.com/article/list/?page='
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
        }





    def loadpage(self,url):
        response = requests.get(url=url,headers=self.headers)
        content = response.content.decode('utf-8')
        html = etree.HTML(content)
        tu = html.xpath('//a[contains(@class,"list-group-item")]')

        for i in tu:
            title = i.xpath('.//div[@class="random_title"]/text()')[0]
            print(title)
            img = i.xpath('.//img[contains(@class,"lazy")]/@data-original')
            # print(img)
            name = 'doutu/' + title
            if not os.path.exists(name):
                os.mkdir(name)
                for j,url in enumerate(img):
                    # self.xiazai(name,j,url)
                    print(j,url)



    def xiazai(self,name,j,url):

        response = requests.get(url=url,headers=self.headers)

        content = response.content

        self.cunru(name,j,url,content)



    def cunru(self,name,j,url,content):
        filename = name + '/' + str(j) + '-' + url[-10:]
        with open(filename,'wb') as f:
            f.write(content)



    def main(self):
        url = self.url + str(self.page)
        self.loadpage(url)





if __name__ == "__main__":
    d = doutu()
    d.main()