# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import pymysql


class TengxunPipeline(object):

    def __init__(self, host, port, user, pwd, db):
        self.client = pymysql.Connect(host, user, pwd, db, port, charset='utf8')
        self.cursor = self.client.cursor()

    @classmethod
    def from_crawler(cls, crawler):
        host = crawler.settings['MYSQL_HOST']
        port = crawler.settings['MYSQL_PORT']
        user = crawler.settings['MYSQL_USER']
        pwd = crawler.settings['MYSQL_PWD']
        db = crawler.settings['MYSQL_DB']

        return cls(host, port, user, pwd, db)

    def process_item(self, item, spider):
        insert_sql = """
               insert into zhaopin(title,types,num,didian,times)
               VALUE (%s, %s, %s, %s, %s)
        """
        try:
            self.cursor.execute(insert_sql, (item['title'], item['types'], item['num'], item['didian'], item['times']))
            self.client.commit()
        except Exception as err:
            print(err)
            self.client.rollback()
        return item

# class TengxunPipeline(object):
#     def __init__(self):
#         self.f = open('tengxun.json','a')
#
#
#     def process_item(self, item, spider):
#         self.f.write(json.dumps(dict(item),ensure_ascii=False)+'\n')
#         return item
#
#
#     def teng_close(self,spider):
#         self.f.close()
