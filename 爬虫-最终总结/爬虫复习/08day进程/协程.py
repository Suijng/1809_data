# 1.可迭代对象?
# 判断对象是否是可迭代对象
from collections import Iterable
# data = [1,2,3,4,5,6]
data = 'string'
print(isinstance(data,Iterable))


# 2.迭代器?
# 迭代器是一个可以记住遍历位置的对象,迭代器对象从第一个元素开始访问,直到所有的元素都被访问完毕是结束,
# 迭代器只能向前不能向后,迭代器内部都有__iter__和__next__方法

class BooKList(object):

    def __init__(self,num):
        self.num = num
        self.current = 0

    def __iter__(self):
        '''拥有这个方法,说明是一个可迭代对象'''
        return self

    def __next__(self):
        '''取值操作'''
        if self.current < self.num:
            self.current += 1
            return self.current
        else:
            # 停止迭代
            raise StopIteration

for i in range(10):
    # print(i)
    pass

# 3.生成器?
# 生成器是一个特殊的迭代器
# 创建生成的方式一:
data = (i for i in (1,2,3,4,5,6,7,8,9) if i < 5)
print(data)
# 得到一个生成器 床架一个生成器
# data = <generator object <genexpr> at 0x7f0f9ab57410>

# 创建生成器方式二:
def range(start=None,end=None):

    start = start if start else 0
    while start < end:
        yield start
        start += 1

# data = range(0,100)
# print(data)
# for i in data:
#     print(i)

# data = []
# for i in range(1,10):
#     data.append(i)
#     print(data)

# def run1():
#     num = 0
#     while True:
#         yield '执行run 1' + '' + str(num)
#         num +=1
#
# def run2():
#     num = 0
#     while True:
#         yield '执行run 2' + '' + str(num)
#         num += 1
#
# if __name__ == '__main__':
#     obj1 = run1()
#     obj2 = run2()
#     while True:
#         print(next(obj1,obj2))

# 4.协程?
#
from greenlet import greenlet
import requests

def download1(url=None):
    print(url,'download1开始请求')
    response = requests.get(url)

    gl2.switch('https://www.baidu.com/')
    if response.status_code == 200:
        print('download1请求成功')
        gl2.switch()

def download2(url=None):
    print(url,'download2开始请求')
    response = requests.get(url)

    gl1.switch()
    if response.status_code == 200:
        print('download2请求成功')


# 作用greenlent创建协程
gl1 = greenlet(download1)
gl2 = greenlet(download2)

# switch完成携程之间的切换
gl1.switch('https://www.baidu.com/')


######## gevent ######
import gevent
def download1(url=None):
    print(url, 'download1开始请求')
    response = requests.get(url)
    gevent.sleep(2)
    if response.status_code == 200:
        print('download1请求成功',response.url)

# 创建协程
gl1 = greenlet(download1,'https://www.baidu.com/?p=1')
gl2 = greenlet(download1,'https://www.baidu.com/?p=2')
gl3 = greenlet(download1,'https://www.baidu.com/?p=3')


########  协程池  ##########
from gevent import monkey,pool
monkey.patch_all() # 补丁,让耗时操作转换为gevent内部能够识别的模块
import gevent

# 创建一个协程池
pool = pool.Pool(4)

gevent.joinall([
    pool.spawn(download1,'https://www.baidu.com/?p=1'),
    pool.spawn(download1,'https://www.baidu.com/?p=2'),
    pool.spawn(download1,'https://www.baidu.com/?p=3'),
    pool.spawn(download1,'https://www.baidu.com/?p=4'),
    pool.spawn(download1,'https://www.baidu.com/?p=5'),
    pool.spawn(download1,'https://www.baidu.com/?p=6'),
    pool.spawn(download1,'https://www.baidu.com/?p=7'),
    pool.spawn(download1,'https://www.baidu.com/?p=8'),
])

