# 第一种方式创建进程池
#
# from concurrent.futures import ProcessPoolExecutor
# import requests
#
# def task(url):
#     headers = {
#         'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36'
#     }
#     response = requests.get(url,headers=headers)
#     if response.status_code == 200:
#         return response.text,response.status_code
#
# def done_task(future):
#
#     text,code = future.result()
#     print(len(text),code)
#
#
#
# if __name__ == '__main__':
#
#     process_pool = ProcessPoolExecutor(8)
#
#     for i in range(1,101):
#         url = 'https://www.baidu.com/?=p' + str(i)
#         # 往往进程池中添加执行函数,和执行函数相关参数
#         result = process_pool.submit(task,url)
#         result.add_done_callback(done_task)
#
#     # 等待进程池中所有的任务都结束在去执行
#     process_pool.shutdown()
#     print('任务都执行完毕了')





# 第二种方式
from multiprocessing import Pool
import requests

def task(url):
    headers = {
        'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36'
    }
    response = requests.get(url,headers=headers)
    if response.status_code == 200:
        return response.text,response.status_code

def done_task(future):
    # print(future)
    # future:执行函数返回什么,我们就接收什么
    text = future[0]
    code = future[1]
    print(len(text),code)


if __name__ == '__main__':

    # 创建进程池
    process_pool = Pool(8)

    for i in range(1,101):
        url = 'https://www.baidu.com/?p='+str(i)
        # apply_async:异步的方式添加执行任务
        process_pool.apply_async(task,args=(url),callback=done_task)
        # apply:同步的方式添加任务
        process_pool.apply()

    # 关闭进程池
    process_pool.close()
    # 阻塞进程作用
    process_pool.join()

    print('全部任务执行完毕')
