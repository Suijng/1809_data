# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

import random
import base64
from scrapy import signals
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from scrapy.http import HtmlResponse


class TengxunSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class TengxunDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


#UA中间件
class RandomUserAgent(object):
    def process_request(self, request, spider):
        # 获取到代理的代理池
        useragents = spider.settings['USERAGENTS']

        # 随机获取一个User-Agent
        user_agent = random.choice(useragents)

        print(user_agent)

        if user_agent:
            request.headers['User-Agent'] = user_agent
            # 赋值的两种方式
            # request.headers.setdefault(b'User-Agent', user_agent)



#设置代理中间件
class RandomProxyMiddleware(object):
    def process_request(self, request, spider):

        proxies = spider.settings['PROXIES']
        proxy = random.choice(self.proxies)
        if proxy['user_pwd'] is None:
            # 没有代理账户验证的代理使用方式
            request.meta['proxy'] = proxy['ip_port']
        else:
            #对账户密码进行base64编码
            user_pwd = base64.b64encode(proxy['user_pwd'].encode('utf-8')).decode('utf-8')
            #对应到代理服务器的信令格式里
            request.headers['Proxy-Authorization'] = 'Basic ' + user_pwd
            request.meta['proxy'] = proxy['ip_port']




#设置cookis中间件
class RandomCookiesMiddleware(object):
    def process_request(self, request, spider):
        cookies = spider.settings['COOKIES']
        # 随机获取一个cookies
        cookie = random.choice(cookies)
        if cookie:
            request.cookies = cookie



#设置selenium中间件
class SeleniumMiddleware(object):
    def __init__(self):

        self.drive = webdriver.Chrome(executable_path='')
        self.drive.set_page_load_timeout(10)

    def process_request(self,request,spider):
        try:
            url = request.url
            self.drive.get(url)
            if self.drive.page_source:
                return HtmlResponse(url=url,body=self.drive.page_source,status=200,encoding='utf-8',request=request)
        except TimeoutException:
            print('请求超时')
            return HtmlResponse(url=url,body=None,status=500)




