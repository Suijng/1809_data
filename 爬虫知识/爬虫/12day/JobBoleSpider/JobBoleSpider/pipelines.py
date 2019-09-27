# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import os
import scrapy
from scrapy.contrib.pipeline.images import ImagesPipeline
from scrapy.utils.project import get_project_settings

class JobbolespiderPipeline(object):
    def __init__(self):
        self.f = open('bole.json','a')


    def process_item(self, item, spider):
        self.f.write(json.dumps(dict(item),ensure_ascii=False)+'\n') #防止出现乱码
        return item


    def stop(self,spider):
        self.f.close()


IMAGES_STORE = get_project_settings().get('IMAGES_STORE')
class JobboleImgspiderPipeline(ImagesPipeline):

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

            item['path'] = IMAGES_STORE + item['title'] + '.jpg'
        else:
            item['path'] = ''

        return item




