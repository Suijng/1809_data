# -*- coding: utf-8 -*-
import scrapy
from ShuangSeqiu.items import ShuangseqiuItem

class KaijiangSpider(scrapy.Spider):
    name = 'kaijiang'
    allowed_domains = ['kaijiang.500.com']
    start_urls = ['http://kaijiang.500.com/shtml/ssq/19002.shtml']

    def parse(self, response):
        # item = ShuangseqiuItem()
        se_url = response.xpath('//div[@class="iSelectList"]//a/@href').extract()
        for url in se_url:
            yield scrapy.Request(url=url,callback=self.zhongjiang)


    def zhongjiang(self,response):
        # item = response.meta.get('item')
        item = ShuangseqiuItem()
        times = response.xpath('//span[@class="span_right"]/text()').extract_first('')
        hong = ','.join(response.xpath('//div[@class="ball_box01"]/ul//li/text()').extract())[:-3]
        lan = ','.join(response.xpath('//div[@class="ball_box01"]/ul//li/text()').extract())[-2:]

        item['times'] = times
        item['hong'] = hong
        item['lan'] = lan
        yield item
