# -*- coding: utf-8 -*-
import scrapy
from PengFuSpider.items import PengfuspiderItem


class PengfuSpider(scrapy.Spider):
    #爬虫的名字
    name = 'pengfu'
    #爬虫范围
    allowed_domains = ['pengfu.com']

    url = 'https://www.pengfu.com/xiaohua_'
    page = 1
    #起始URL
    start_urls = [url + str(page) + '.html']

    jokes=[]

    def parse(self, response):

        div_list = response.xpath('//div[@class="list-item bg1 b1 boxshadow"]')
        print(div_list)
        for div in div_list:
            item = PengfuspiderItem()
            title = div.xpath('.//h1/a/text()').extract()[0].strip()
            content = div.xpath('.//div[@class="content-img clearfix pt10 relative"]/text()').extract()[0].strip()
            item['title'] = title
            item['content'] = content
            yield item

            # self.jokes.append(item)
            # print('标题:' + title)
            # print('内容:' + content + '\n\n')

        if self.page <= 1:
            self.page += 1
            print(self.url + str(self.page) + '.html')
            yield scrapy.Request(url = self.url + str(self.page) + '.html',callback=self.parse)


    '''
    
    scrapy startproject xxx 创建爬虫项目
    
    scrapy genspider pengfu pengfu.com 进入项目 创建爬虫文件
    
    scrapy crawl pengfu 开始爬虫 执行
    
    response.body 相当于 requests 里面的response.content
    
    response.text 相当于 request 里面的response.text
    
    extract() 把内容转成unicode字符串
    
    
    
    '''

