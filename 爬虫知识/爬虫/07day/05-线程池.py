from concurrent.futures import ThreadPoolExecutor
import requests
from lxml import etree

#声明一个线程池
pool = ThreadPoolExecutor(3)

headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
        }

#声明一个函数
def job_request(args):
    url = args[0]
    print(url)
    response = requests.get(url=url,headers=headers)
    return response.text


#解析函数
def parse(future):
    result = future.result()
    html = etree.HTML(result)
    name = html.xpath('//a[@class="archive-title"]/text()')
    print(name)

for i in range(1,30):
    #提交任务
    full_url = 'http://blog.jobbole.com/all-posts/page/' + str(i)
    p = pool.submit(job_request,(full_url,))
    p.add_done_cllback(parse)



