# -*- coding: utf-8 -*-
import scrapy
from ChuFangSpider.items import ChufangspiderItem

class ChufangSpider(scrapy.Spider):
    name = 'chufang'
    allowed_domains = ['xiachufang.com']

    url = 'http://www.xiachufang.com'
    start_urls = [url + '/category/40076/']

    def parse(self, response):

        div_list = response.xpath('//div[@class="pure-u-3-4 category-recipe-list"]//ul[@class="list"]//li')
        for div in div_list:
            item = ChufangspiderItem()

            title_url = div.xpath('.//p[@class="name"]/a/@href').extract_first('')
            url = self.url + title_url

            item['url'] = url

            yield scrapy.Request(url=url,callback=self.xiangqing,meta={'item':item})



    def xiangqing(self,response):
        item = response.meta.get('item')

        title = response.xpath('//h1/text()').extract_first('')
        img = response.xpath('//div[@class="cover image expandable block-negative-margin"]/img/@src').extract_first('')

        yongliao = ''.join(response.xpath('//div[@class="ings"]//tr//text()').extract()).replace('\n','')

        zuofa = ''.join(response.xpath('//div[@class="steps"]/ol//li//p/text()').extract())

        item['title'] = title
        item['img'] = img
        item['yongliao'] = yongliao
        item['zuofa'] = zuofa

        yield item
        # print(item)





