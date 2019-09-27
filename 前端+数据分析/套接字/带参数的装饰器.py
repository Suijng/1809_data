
# 同一个装饰器 验证不同函数 不同的级别
def set_level(level_num):
    def set_func(func):
        def call_func(*args,**kwargs):
            if level_num == 10:
                print('--权限级别1,验证--')
            elif level_num == 2:
                print('--权限级别2,验证--')
            return func()
        return call_func
    return set_func


# 1.调用set_func并且将1当做实参传递
# 2.用上一步调用的返回值,当做装饰器对test1函数进行装饰
@set_level(10) # 给test1 验证了一个权限的东西
def test1():
    print('--test1--')
    return 'ok'


@set_level(2) # 给test2 验证了一个权限的东西
def test2():
    print('--test2--')
    return 'ok'


test1()
test2()
