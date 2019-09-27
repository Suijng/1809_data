from selenium import webdriver
from lxml import etree
import re
import time

# 创建chrome参数对象
opt = webdriver.ChromeOptions()

#把chrome设置成为无界面模式
opt.set_headless()

#创建chrome无界面对象
drive = webdriver.Chrome(
    options=opt, executable_path='/home/sj/桌面/爬虫/chromedriver'
)

# drive = webdriver.Chrome(executable_path='/home/sj/桌面/爬虫/chromedriver')


drive.get('https://www.douyu.com/g_jdqscjzc')


    # pattren = re.compile('<p>.*?<span.*?<span.*?class="dy-num.*?">(\d+).*?</p>')
    # num = pattren.findall(i.text)

page = 1
z_num = 0
g_num = 0
while True:
    time.sleep(1)
    html = etree.HTML(drive.page_source)
    da = html.xpath('//div[@class="mes"]')
    for i in da:
        title = i.xpath('.//div[@class="mes-tit"]/h3/text()')[0].replace(' ', '')
        num = i.xpath('.//span[@class="dy-num fr"]/text()')[0]
        if num[-1] == '万':
            z_num+=1
            g_num+=float(num[:-1])*10000
        else:
            g_num+=float(num)
        dic = {
            'num': num,
            'title': title,
        }
        print(dic)

    xiayiye = drive.page_source.find('shark-pager-disable-next')
    if xiayiye == -1:
        drive.find_element_by_class_name('shark-pager-next').click()
        page+=1
    else:
        print('正在打印页:%d'%page)
        print('正在直播:%d'%z_num)
        print('正在观看:%d'%g_num)
        break








