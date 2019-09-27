# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from TengXun.items import TengxunItem


class TencentSpider(CrawlSpider):
    name = 'tencent'
    allowed_domains = ['tencent.com']
    start_urls = ['https://hr.tencent.com/position.php?&start=0']

    rules = (
        Rule(LinkExtractor(allow=r'start=\d+'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        tr_list1 = response.xpath('//tr[@class="even"]')
        tr_list2 = response.xpath('//tr[@class="odd"]')
        tr_list = tr_list1 + tr_list2

        for tr in tr_list:
            item = TengxunItem()
            title = tr.xpath('./td[1]/a/text()').extract_first()
            types = tr.xpath('./td[2]/text()').extract_first()
            num = tr.xpath('./td[3]/text()').extract_first()
            didian = tr.xpath('./td[4]/text()').extract_first()
            times = tr.xpath('./td[5]/text()').extract_first()

            item['title'] = title
            item['types'] = types
            item['num'] = num
            item['didian'] = didian
            item['times'] = times

            yield item



