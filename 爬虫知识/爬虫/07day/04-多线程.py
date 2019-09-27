import requests
from threading import Thread
from lxml import etree
import queue


class crawlSpider(Thread):
    def __init__(self,name,page_queue,data_queue):
        super(crawlSpider,self).__init__()
        self.name = name,
        self.page_queue = page_queue,
        self.data_queue = data_queue,

        self.headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
        }

    def run(self):
        #从page_queue获取对应的页码
        while not self.page_queue.empty():
            page = self.page_queue.get()
            url = 'http://blog.jobbole.com/all-posts/page/' + str(page)
            response = requests.get(url=url,headers=self.headers)
            self.data_queue.put(requests.text)




class parseSpider(Thread):
    def __init__(self):
        super(parseSpider,self).__init__()

    def run(self):
        while not self.data_queue.empty():
            html = etree.HTML(self.data_queue.get())
            name = html.xpath('//div[@class="post-meta"]/p')
            for item in name:
                title = item.xpath('./a[1]/text()')
                print(title)

                # 加锁
                self.lock.acquire()
                with open('jobbole.txt', 'a') as f:
                    f.write(title + '\n')
                # 解锁
                self.lock.release()



def spider():
    page_queue = queue.Queue(30)
    #数据队列
    data_queue = queue.Queue()

    for i in range(1,31):
        page_queue.put(i)

    thread_name = ['一号','二号','三号']
    t_list = []
    for name in thread_name:
        #创建线程
        t = crawlSpider(name=name,page_queue=page_queue,data_queue=data_queue)
        t.start()
        t_list.append(t)

    for t in t_list:
        t.join()#当线程执行完毕 在往下走

    parse_name = ['解析一号','解析二号','解析三号']
    for name in parse_name:
        name.parseSpider(name,data_queue)
        name.start()



if __name__== '__main__':
    spider()