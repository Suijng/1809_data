# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from XiaChufang.items import XiachufangItem

class ChufangSpider(CrawlSpider):
    name = 'chufang'
    allowed_domains = ['xiachufang.com']
    start_urls = ['http://www.xiachufang.com/category/40076/']

    rules = (
        Rule(LinkExtractor(allow=r'/category/\d+/'), callback='parse_item', follow=True),
        Rule(LinkExtractor(allow=r'/recipe/\d+/'), callback='parse_item', follow=False),
    )

    def parse_item(self, response):

        item = XiachufangItem()
        title = response.xpath('//h1/text()').extract_first('')

        item['title'] = title
        print(item)

        yield item




