# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from YouXin.items import YouxinItem


class YouxinSpider(CrawlSpider):
    name = 'youxin'
    allowed_domains = ['xin.com']
    start_urls = ['https://www.xin.com/beijing/baoma/']

    rules = (
        Rule(LinkExtractor(allow=r'/beijing/baoma/i\d+/'), callback='parse_item', follow=True),
        Rule(LinkExtractor(allow=r'/che\d+.html'), callback='parse_item', follow=False),
    )

    def parse_item(self, response):
        item = YouxinItem()
        name = response.xpath('//div[@class="cd_m_h cd_m_h_zjf"]/span/text()').extract_first('')
        num = response.xpath('//span[@class="cd_m_info_jg"]/b/text()').extract_first('')

        item['name'] = name
        item['num'] = num

        yield item

        print(name,num)