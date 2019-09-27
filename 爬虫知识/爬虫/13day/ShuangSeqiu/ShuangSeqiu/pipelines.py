# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

# import pymongo
import pymysql


class ShuangseqiuPipeline(object):

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
               insert into zhaopin(times,hong,lan)
               VALUE (%s, %s, %s)
        """
        try:
            self.cursor.execute(insert_sql, (item['times'], item['hong'], item['lan']))
            self.client.commit()
        except Exception as err:
            print(err)
            self.client.rollback()
        return item























    # def __init__(self,host,port,dbname,sheetname):
    #     # 创建MONGODB数据库链接
    #     client = pymongo.MongoClient(host=host, port=port)
    #     # 指定数据库
    #     mydb = client[dbname]
    #     # 存放数据的集合名称
    #     self.mysheet = mydb[sheetname]
    #
    #
    # @classmethod
    # def from_crawler(cls, crawler):
    #     host = crawler.settings["MONGODB_HOST"]
    #     port = crawler.settings["MONGODB_PORT"]
    #     dbname = crawler.settings["MONGODB_DBNAME"]
    #     sheetname = crawler.settings["MONGODB_SHEETNAME"]
    #
    #     return cls(host, port, dbname, sheetname)
    #
    #
    # def process_item(self, item, spider):
    #     data = dict(item)
    #     # mongodb数据插入语句，使用save保存数据的效率会很慢，因为它需要循环便利，操作费时
    #     self.mysheet.insert(data)
    #     return item
