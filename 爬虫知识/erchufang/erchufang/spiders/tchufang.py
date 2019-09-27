# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy_redis.spiders import RedisSpider
from scrapy_redis.spiders import RedisCrawlSpider
from erchufang.items import ErchufangItem

class TchufangSpider(RedisCrawlSpider):
    name = 'erchufang'
    #allowed_domains = ['xiachufang.com']
    redis_key = 'chufang:start_urls'
    #start_urls = ['http://www.xiachufang.com/category/40076/']

    rules = (
        Rule(LinkExtractor(allow=r'/category/\d+/'), follow=True)
        ,Rule(LinkExtractor(allow=r'/recipe/\d+/'), callback='parse_item', follow=False),

    )


    def parse_item(self, response):
        dange = response.xpath('//div[@class="cover pure-u"]/img/@src').extract_first()
        cai = response.xpath('//h1[@class="page-title"]/text()').extract_first()
        item=ErchufangItem()
        item['cai']=cai

        yield item

