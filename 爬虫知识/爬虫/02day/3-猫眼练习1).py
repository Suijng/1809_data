import urllib.request
import urllib.parse
import re


class maoyan():
    def __init__(self):
        self.url = 'https://maoyan.com/board/4'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
        }

    def loadpage(self, url):
        request = urllib.request.Request(url=self.url, headers=self.headers)
        response = urllib.request.urlopen(request)
        # print(response.status)

        content = response.read().decode()
        my = re.compile(r'<dd>.*?<i.*?class="board-index.*?>(.*?)</i>.*?' +
                        '<img.*?<img.*?data-src="(.*?)".*?class="board-img".*?>.*?' +
                        '<a.*?>(.*?)</a>.*?' +
                        '<p.*?class="star">(.*?)</p>.*?' +
                        '<p.*?class="releasetime">(.*?)</p>.*?' +
                        '<i.*?class="integer">(.*?)</i>' +
                        '<i.*?>(.*?)</i>'
                        , re.S)
        m = my.findall(content)
        for i in m:
            for j in i:
                print(j)
                self.xieru(j)

    def xieru(self, j):
        with open('maoyan.html', 'a') as f:
            f.write(j)

    def main(self):
        start = int(input('输入起始页'))
        end = int(input('输入终止页'))
        for i in range(start, end + 1):
            url = self.url + urllib.parse.urlencode({'offset': str((i - 1) * 10)})
            self.loadpage(url)


if __name__ == '__main__':
    m = maoyan()
    m.main()
