from lxml import etree
import requests


class tieba():
    def __init__(self):
        self.url = 'https://tieba.baidu.com'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
        }



    def loadpage(self,url):
        response = requests.get(url=url)
        html = response.content.decode('utf-8')
        content = etree.HTML(html)
        lis = content.xpath('//div[@class="threadlist_title pull_left j_th_tit "]/a/@href')
        for i in lis:
            tp = self.url+i
            self.tupian(tp)



    def tupian(self,url):
        response = requests.get(url=url)
        html = response.content.decode('utf-8')
        content = etree.HTML(html)

        lis = content.xpath('//img[@class="BDE_Image"]/@src')
        # print(lis)
        for i in lis:
            # print(i)
            self.xiazai(i)



    def xiazai(self,url):
        # print(url)
        response = requests.get(url=url)
        img = response.content
        # print(img)
        print('正在下载...')
        self.cunru(img,url)


    def cunru(self,img,lis):
        print('正在储存...')
        print('')
        filename = 'tieba/' + lis[-10:] +'.jpg'
        with open(filename,'wb') as f:
            f.write(img)




    def main(self):
        kw = input('请输入爬的名字:')
        start = int(input('请输入起始页:'))
        end = int(input('请输入终止页:'))
        for i in range(start,end+1):
            url = self.url + '/f?' + 'kw=' + kw + '&' + 'pn=' + str((end-1)*50)
            self.loadpage(url)




if __name__ == '__main__':
    t = tieba()
    t.main()