import urllib.request
import re
import urllib.parse


class fu():
    def __init__(self):
        self.url = "http://www.budejie.com/audio/"
        self.headers = {

            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"
        }

    def loadpage(self, url):

        request = urllib.request.Request(url=url, headers=self.headers)

        response = urllib.request.urlopen(request)

        content = response.read().decode()

        pattern = re.compile(r'<li.*?class="j-r-list-tool-l-down f-tar j-down-video j-down-hide ipad-hide".*?<a.*?href="(.*?)".*?>.*?</a>.*?</li>',re.S)

        er = pattern.findall(content)
        for i in er:
            self.haha(i)
    def haha(self,i):
        filename = "yinyue/" + i[-15:]

        with open(filename, 'a') as f:
            f.write(i)



    def statit(self):
        url = "http://www.budejie.com/audio/"
        self.loadpage(url)



if __name__ == "__main__":
    a = fu()
    a.statit()
























