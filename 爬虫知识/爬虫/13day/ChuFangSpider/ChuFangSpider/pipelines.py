# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import os
import scrapy
import pymongo
from scrapy.contrib.pipeline.images import ImagesPipeline
from scrapy.utils.project import get_project_settings


# class ChufangspiderPipeline(object):
#     def __init__(self):
#         self.f = open('chufang.json','a')
#
#
#     def process_item(self, item, spider):
#         self.f.write(json.dumps(dict(item),ensure_ascii=False)+'\n')
#         return item
#
#
#     def jieshu(self,spider):
#         self.f.close()




class ChufangspiderPipeline(object):
    def __init__(self,host,port,dbname,sheetname):
        # 创建MONGODB数据库链接
        client = pymongo.MongoClient(host=host, port=port)
        # 指定数据库
        mydb = client[dbname]
        # 存放数据的集合名称
        self.mysheet = mydb[sheetname]

    @classmethod
    def from_crawler(cls, crawler):
        host = crawler.settings["MONGODB_HOST"]
        port = crawler.settings["MONGODB_PORT"]
        dbname = crawler.settings["MONGODB_DBNAME"]
        sheetname = crawler.settings["MONGODB_SHEETNAME"]

        return cls(host, port, dbname, sheetname)



    def process_item(self, item, spider):
        data = dict(item)
        # mongodb数据插入语句，使用save保存数据的效率会很慢，因为它需要循环便利，操作费时
        self.mysheet.insert(data)
        return item










IMAGES_STORE = get_project_settings().get('IMAGES_STORE')
class ChufangImgspiderPipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        #发起图片请求 把结果回调给item_completed
        return scrapy.Request(url=item['img'])

    def item_completed(self, results, item, info):
        # for ok,x in results:
        #     if ok:
        #         x['path']
        imgs = [x['path'] for ok,x in results if ok]
        if imgs:
            os.rename(IMAGES_STORE + imgs[0],
                      IMAGES_STORE + item['title'] + '.jpg')

            item['path'] = os.getcwd() + '/' + IMAGES_STORE + item['title'] + '.jpg'
        else:
            item['path'] = ''

        return item