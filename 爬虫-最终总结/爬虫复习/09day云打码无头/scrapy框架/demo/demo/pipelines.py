# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exceptions import DropItem
import pymysql

class DemoPipeline(object):

    def __init__(self):
        self.client = pymysql.Connect(
            '127.0.0.1','root','l',
            'class1809_scrapy',3306,charset='utf8'
        )
        self.cursor = self.client.cursor()


    def process_item(self, item, spider):
        if len(item.name) == 0:
            raise DropItem('没有获取到名字')

        # 储存数据
        data = dict(item)
        sql = item.get_sql_str(data)

        try:
            self.cursor.execute(sql,list(data.values()))
            self.cursor.commit()
        except Exception as e:
            print(e)
            self.client.rollback()

        return item

    def close_spider(self,spider):
        # 可选方法,只有爬虫结束的时候会执行一次
        self.client.close()
        self.cursor.close()