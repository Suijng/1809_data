# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JobbolespiderItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    desc = scrapy.Field()
    content = scrapy.Field()
    url = scrapy.Field()
    img = scrapy.Field()
    path = scrapy.Field()

