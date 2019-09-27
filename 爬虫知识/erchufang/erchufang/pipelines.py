# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
class ErchufangPipeline(object):
    def __init__(self):
        self.f = open('cai.json', 'a')


    def process_item(self, item, spider):
        self.f.write(json.dumps(dict(item), ensure_ascii=False) + '\n')
        return item

    def process_close(self, spider):
        self.f.close()
