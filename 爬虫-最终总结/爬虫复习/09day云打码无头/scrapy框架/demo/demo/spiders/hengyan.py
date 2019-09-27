# -*- coding: utf-8 -*-
import scrapy
from demo.items import DemoItem
from scrapy.http import Response,Request


class HengyanSpider(scrapy.Spider):
    name = 'hengyan'
    # 设置爬去的域 (可以设置多个)
    allowed_domains = ['hengyan.com']
    # 设置起始url地址
    start_urls = ['http://top.hengyan.com/mianfei/default.aspx?p=1']


    def parse(self, response):
        # 解析起始url的响应结果
        # print(response.url,response.status,response.text)
        urls = response.xpath('//a[@class="bn"]/@href').extract()
        # print(urls)
        for url in urls:
            yield scrapy.Request(
                url = url,
                callback=self.parse_detail,
                meta={'url':url}
            )

    def parse_detail(self,response):
        '''解析详情数据'''
        url = response.meta['url']
        # 取数据
        item = DemoItem()
        item['name'] = response.xpath('//h2/text()').extract_first('')
        item['point_nums'] = response.xpath('//p[@class="info"]/span[1]/text()').re('\d+')[0]
        item['category'] = response.xpath('//p[@class="info"]//span[2]/a/text()').extract_first('')
        item['size'] = response.xpath('//p[@class="info"]//span[3]/text()').re('\d+')[0]
        item['other'] = response.xpath('//p[@class="info"]//span[4]/text()').extract_first('')
        item['content'] = ''.join(response.xpath('//div[@class="des"]/p[2]/text()').extract())

        print(item)
        yield item


    # def parse(self, response):
    #     # 解析起始url的响应结果
    #     pass
