
'''
def outside1(test):

    def inside():
        print('welcome')
        return test()
    return inside

def func():
    print('hello world')


a = outside1(func)
a()
'''

'''
# 装饰器
def outside1(test):

    def inside():
        print('welcome')
        return test()
    return inside

@outside1
def func():
    print('hello world')

func()

# a = outside1(func)
# a()
'''

'''
# 给函数传参数
def outside1(test):
    def inside(a,b):
        print('welcome')
        return test(a,b)
    return inside

@outside1
def func(a,b):
    print(a+b)

func(1,2)
'''

'''
# 传很多参数的时候
def outside1(test):
    def inside(*args,**kwargs):
        print('welcome')
        return test(*args,**kwargs)
    return inside

@outside1
def func(*args,**kwargs):
    print(*args,**kwargs)

func([1,2,3])
'''

# 多个装饰器 执行从下往上 调用从上网往下
def outside1(test):
    def inside(*args,**kwargs):
        print('执行了装饰器外部函数2')
        print('welcome1')
        return test(*args,**kwargs)
    return inside

def outside2(test):
    def inside(*args,**kwargs):
        print('执行了装饰器外部函数1')
        print('welcome2')
        return test(*args,**kwargs)
    return inside

@outside1
@outside2
def func(*args,**kwargs):
    print(kwargs)

func(a=1,b=2)