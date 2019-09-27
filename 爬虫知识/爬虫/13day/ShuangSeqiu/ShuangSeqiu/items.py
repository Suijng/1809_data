# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ShuangseqiuItem(scrapy.Item):
    # define the fields for your item here like:
    url = scrapy.Field()
    times = scrapy.Field()
    hong = scrapy.Field()
    lan = scrapy.Field()
