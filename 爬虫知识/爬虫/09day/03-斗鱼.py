from selenium import webdriver
from lxml import etree
import re

drive = webdriver.Chrome(executable_path='/home/sj/桌面/爬虫/chromedriver')


drive.get('https://www.douyu.com/g_jdqscjzc')


html = etree.HTML(drive.page_source)


da = html.xpath('//div[@class="mes"]')
for i in da:
    title = i.xpath('.//div[@class="mes-tit"]/h3/text()')[0].replace(' ','')
    # num = i.xpath('.//span[@class="dy-num fr"]/text()')[0]

    pattren = re.compile('<p>.*?<span.*?<span.*?class="dy-num.*?">(\d+).*?</p>')
    num = pattren.findall(i.text)

    # dic = {
    #     'num' : num,
    #     'title' : title,
    # }
    print(num)






