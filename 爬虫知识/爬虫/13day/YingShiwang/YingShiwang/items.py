# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class YingshiwangItem(scrapy.Item):
    # define the fields for your item here like:

    # 片名
    name = scrapy.Field()
    # 上映日期
    date = scrapy.Field()
    # 时长
    time = scrapy.Field()
    # 类别
    type = scrapy.Field()
    # 主演
    zy = scrapy.Field()
    # 简介
    jj = scrapy.Field()
    # 种子
    ed2k = scrapy.Field()
    # 地址
    href = scrapy.Field()


    # li_url = scrapy.Field()
    # jianjie = scrapy.Field()
