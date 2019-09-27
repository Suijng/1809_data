from concurrent.futures import ProcessPoolExecutor
import requests
from lxml import etree

pool = ProcessPoolExecutor(3)

headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
        }


def run(age):
    url = age[0]
    print(url)





def done():
    pass


for i in range(1,11):
    full_url = 'http://www.xiaohuar.com/list-1-' + str((i)-1) + '.html'
    handle = pool.submit(run,(i,))
    handle.add_done_callback(done)

