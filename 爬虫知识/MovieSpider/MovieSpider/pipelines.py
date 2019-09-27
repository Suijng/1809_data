# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json


class MoviespiderPipeline(object):

    def __init__(self):
        self.movies = []#

        self.f = open("movie.json", "a")

    def process_item(self, item, spider):
        # self.movies.append(item)
        self.f.write(json.dumps(dict(item), ensure_ascii=False) + "\n")

        return item

    def close_spider(self, spider):
        #self.f.write(json.dumps(self.movies, ensure_ascii=False) + "\n")
        self.f.close()
