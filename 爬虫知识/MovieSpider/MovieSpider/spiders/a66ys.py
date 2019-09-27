# -*- coding: utf-8 -*-
import scrapy
import math
import re
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy_redis.spiders import RedisCrawlSpider
from MovieSpider.items import MoviespiderItem


class A66ysSpider(RedisCrawlSpider):
    name = '66ys'
    # allowed_domains = ['66ys.tv']
    redis_key = 'chufang:start_urls'
    # start_urls = ['https://www.66ys.tv/']

    def parse(self, response):
        div_list = response.xpath('//div[@class="channeltype"]')

        # 所有类型的多少部

        nums = response.xpath('//span[contains(@id,"span_b")]/text()').extract()

        # ["2527","1638"]

        # 每个div都是一个电影类型  对应的也是nums数字
        for position, div in enumerate(div_list):
            # 类型
            type = div.xpath("./h2/a/text()").extract_first("")

            # 更多的地址
            href = div.xpath("./h2/a/@href").extract_first("")

            # 每个类型的页码

            page = math.ceil(int(nums[position]) / 20)
            #
            for i in range(1, page + 1):
                if type == "喜剧片" or type == "动作片" or type == "爱情片" or type == "科幻片" or type == "恐怖片" or type == "战争片" or type == "记录片":
                    full_url = href + "index_" + str(i) + ".html"
                else:
                    full_url = href + "index_" + str(i) + ".htm"

                # #发起第一页的请求
                yield scrapy.Request(url=full_url, callback=self.parselist)

    # 解析列表页的函数
    def parselist(self, response):

        li_list = response.xpath('//div[@class="listBox"]//ul/li')

        for li in li_list:
            # 创建一个电影的item
            item = MoviespiderItem()

            # 取出电影名字
            name = li.xpath('.//h3/a/text()').extract_first("")
            # 电影的类型
            type = li.xpath(".//p[2]/text()").extract_first("")
            # 每个电影的详情页
            href = li.xpath('.//h3/a/@href').extract_first("")

            item["name"] = name
            item["type"] = type.split(":")[1]
            item["href"] = href
            yield scrapy.Request(url=href, callback=self.parsedetail, meta={"item": item})

    def parsedetail(self, response):

        item = response.meta.get("item")
        # 详情页所有内容
        content = "".join(response.xpath('//div[@id="text"]/p/text()').extract())

        content_list = content.split("◎")

        date = ""
        time = ""
        zy = ""
        jj = ""
        ed2k = ""
        for desc in content_list:
            if desc.startswith("上映日期"):
                date = desc.split("期")[1]
            elif desc.startswith("片　　长"):
                time = desc.split("长")[1]
            elif desc.startswith("主　　演"):
                zy = desc.split("演")[1]
            elif desc.startswith("简　　介"):
                jj = desc.split("介")[1]

        pattern = re.compile(r'<a.*?href="(ed2k.*?)">.*?</a>', re.S)

        ed2k_list = pattern.findall(response.text)

        if ed2k_list:
            ed2k = ed2k_list[0]

        item["date"] = date
        item["time"] = time
        item["zy"] = zy
        item["jj"] = jj
        item["ed2k"] = ed2k

        yield item
