import urllib.request
import re


class neihanba():
    def __init__(self):
        self.headers = {
            'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
        }
        self.page = 1 #页数
        self.switch = True #开关


    def loadpage(self,url):
        request = urllib.request.Request(url,headers=self.headers)
        response = urllib.request.urlopen(request) #发起请求

        content = response.read().decode()#读取内容
        title = re.compile(r'<ul.*?class="piclist longList".*?<h4>.*?<b>(.*?)<b>',re.S) #匹配正则
        l = title.findall(content) #提取
        print(l)


    def writepage(self):
        pass


    def main(self):
        url = 'https://www.neihanba.com/dz/'
        self.loadpage(url)
        while self.switch:
            w = input('输入任意键继续,q退出')
            if w == 'q':
                self.switch = False
            else:
                self.page += 1
                url = 'https://www.neihanba.com/dz/list_' + str(self.page) + '.html'
                self.loadpage(url)



if __name__ == '__main__':
    hh = neihanba()
    hh.main()