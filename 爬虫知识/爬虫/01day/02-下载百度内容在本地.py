import urllib.request

url = "https://tieba.baidu.com/f?kw=%C3%C0%C5%AE&fr=ala0&tpl=5"

response = urllib.request.urlopen(url=url)
html = response.read()

# print(response.info()) #请求响应头
# print(response.geturl()) #获取响应地址
# print(response.getcode()) #响应码
# print(response.getheader(name="BDQID")) #获取
# print(response.getheaders()) #获取响应头的数据

# print(html)


with open("tieba.html", "w") as f:
    f.write(html.decode())

