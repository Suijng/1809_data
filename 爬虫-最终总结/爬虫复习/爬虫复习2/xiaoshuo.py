from urllib import request
import re,json


def hengyan(url='http://all.hengyan.com/1/0_0_0_0_0_0_0_0_0_1.aspx'):
    #构建请求头
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36',
    }

    # 添加请求头
    req = request.Request(url=url, headers=headers)
    response = request.urlopen(req, timeout=10)

    content = response.read()
    html = content.decode('utf8')

    pattern = re.compile('<div\sclass="list">(.*?)</div>', re.S)
    list_str = re.findall(pattern, html)[0]
    # print(list_str)

    pattern1 = re.compile('<ul.*?>*?<a.*?href="(.*?)".*?</ul>', re.S)
    ul_strs = re.findall(pattern1, list_str)
    # print(ul_strs)

    for a_url in ul_strs:
        # print(a_url)
        xiangqing(a_url)


def xiangqing(url):
    req = request.Request(url=url)
    response = request.urlopen(req, timeout=10)

    content = response.read()
    html = content.decode('utf8')

    pattern = re.compile('<div\sclass="dh">.*?<label>(.*?)</label>',re.S)
    lable_str = re.findall(pattern,html)[0]
    # print(lable_str)
    # 书号
    pattern1 = re.compile('\d')
    shuzi = re.findall(pattern1,lable_str)
    shuzi_str = ''.join(shuzi)
    # print(shuzi_str)

    pattern2 = re.compile('<div\sclass="hd">.*?<div\sclass="piao">.*?<b>(.*?)</b>'
                          '.*?<span.*?>(.*?)</span>.*?<span.*?>(.*?)</span>'
                          '.*?<div\sclass="jinbi">.*?<p>.*?<span.*?<p>(.*?)</p>'
                          '.*?<li>.*?<p>.*?<span.*?<p>.*?<span.*?>(.*?)</span>.*?</p>'
                          '.*?<div\sclass="des">.*?<h2>(.*?)</h2>'
                          '.*?<p.*?><span>(.*?)</span>'
                          '.*?<span.*?><a.*?>(.*?)</a>'
                          '.*?<span>(.*?)</span>'
                          ,re.S)

    left = re.findall(pattern2,html)
    print(left)






if __name__ == '__main__':

    hengyan()