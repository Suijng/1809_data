import urllib.request
import re

def main():
    url='https://image.baidu.com/search/index?tn=baiduimage&ct=201326592&lm=-1&cl=2&ie=gb18030&word=%C3%C0%C5%AE%CD%BC&fr=ala&ala=1&alatpl=adress&pos=0&hs=2&xthttps=111111'
    response = urllib.request.urlopen(url=url)
    content = response.read().decode('utf-8')
    pattern = re.compile('.*?main_img img-hover.*?data-imgurl="(.*?)">')
    result = re.findall(pattern,content)
    print(result)

if __name__ == '__main__':
    main()