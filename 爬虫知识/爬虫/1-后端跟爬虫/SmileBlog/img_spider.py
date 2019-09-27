import requests
from lxml import etree
import pymysql
import datetime

conn = pymysql.Connect(
    '127.0.0.1', 'root', 'l', '1807_xiaohua', port=3306, charset='utf8'
)
cursor = conn.cursor() #游标 执行sql语句


headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
}



url = 'https://www.pengfu.com/qutu_1.html'

response = requests.get(url=url, headers=headers)
html = etree.HTML(response.text)


div_list = html.xpath('//div[@class="list-item bg1 b1 boxshadow"]')
for div in div_list:
    title = div.xpath('.//h1/a/text()')[0]
    img = div.xpath('.//dd//div[@class="content-img clearfix pt10 relative"]/img/@src')[0]
    num = div.xpath('.//div[@class="fl"]/span[1]//text()')[0]
    print(title,img,num)

    name = 'smile/' + img[-17:]
    file_name = '/home/sj/桌面/爬虫/1-后端跟爬虫/SmileBlog/static/media/' + name
    response = requests.get(url=img, headers=headers)
    with open(file_name, 'wb') as f:
        f.write(response.content)

    sql = 'INSERT INTO SmileApp_photo(title,img,read_num,top,isDelete) values(%s,%s,%s,%s,%s)'
    a = cursor.execute(sql,[title,name,num,0,0])
    try:
        conn.commit()
    except Exception as e:
        conn.rollback()
