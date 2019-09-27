# -*- coding: utf-8 -*-
import scrapy
from JobBoleSpider.items import JobbolespiderItem


class BoleSpider(scrapy.Spider):
    name = 'bole'
    allowed_domains = ['jobbole.com']
    start_urls = ['http://blog.jobbole.com/all-posts/']

    def parse(self, response):
        div_list = response.xpath('//div[@class="post floated-thumb"]')
        for div in div_list:
            item = JobbolespiderItem()
            title = div.xpath('.//a[@class="archive-title"]/text()').extract_first('')
            desc = div.xpath('.//span[@class="excerpt"]/p/text()').extract_first('')
            img = div.xpath('.//div[@class="post-thumb"]/a/img/@src').extract_first('')
            url = div.xpath('.//a[@class="archive-title"]/@href').extract_first('')

            item['title'] = title
            item['desc'] = desc
            item['img'] = img
            item['url'] = url
            print(item)

            yield scrapy.Request(url=url,callback=self.xiangqing,meta={'item':item})


    def xiangqing(self,response):
        item = response.meta.get('item')
        content = ''.join(response.xpath('//div[@class="entry"]//p/text()').extract())

        item['content'] = content

        yield item
