import urllib.request
import re

class xici():
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
        }

    def loadpage(self, url):
        request = urllib.request.Request(url=url,headers=self.headers)
        response = urllib.request.urlopen(request)
        content = response.read().decode()

        dk= re.compile(r'<tr.*?class=".*?>.*?<td.*?class=.*?</td>.*?<td>(.*?)</td>')

        xc = dk.findall(content)
        print(xc)


    def main(self):
        url = 'https://www.xicidaili.com/'
        self.loadpage(url)


if __name__ == '___main_':
    j = xici()
    j.main()


