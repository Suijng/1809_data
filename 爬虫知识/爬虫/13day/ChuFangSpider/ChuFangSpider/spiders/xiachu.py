# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup


class XiachuSpider(scrapy.Spider):
    name = 'xiachu'
    allowed_domains = ['xiachufang.com']
    start_urls = ['http://xiachufang.com/']

    def parse(self, response):
        pass

