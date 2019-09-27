# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ChufangspiderItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    img = scrapy.Field()
    yongliao = scrapy.Field()
    zuofa = scrapy.Field()
    url = scrapy.Field()
    path = scrapy.Field()
