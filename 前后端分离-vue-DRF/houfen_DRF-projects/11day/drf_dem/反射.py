# 什么是反射？
# 通过字符串获取类的属性或者方法

# hasattr(obj,name_str): 判断objec是否有name_str这个方法或者属性
# getattr(obj,name_str): 获取object对象中与name_str同名的方法或者函数
# setattr(obj,name_str,value): 为object对象设置一个以name_str为名的value方法或者属性
# delattr(obj,name_str): 删除object对象中的name_str方法或者属性

def run(self):
    print(self.name,'run')

class User(object):

    def __init__(self,name):
        self.name = name

    def work(self):
        print(self.name,'work')

    def eat(self):
        print(self.name,'eat')


user = User('lisi')

# print(hasattr(user,'name'))
# print(getattr(user,'name'))
# print(setattr(user,'name','wangwu'))
# print(getattr(user,'name'))
#
# print(delattr(user,'name'))
# print(getattr(user,'name','23456'))

# mothod = 'work'
# if hasattr(user,mothod):
#     fun = getattr(user,mothod)
#     if type(fun) == str:
#         print('属性')
#     else:
#         fun()


mothod = 'run'
if hasattr(user,mothod):
    fun = getattr(user,mothod)
    if type(fun) == str:
        print('属性')
    else:
        fun()
else:
    setattr(user,mothod,run)
    fun = getattr(user,mothod)
    if type(fun) == str:
        print('属性')
    else:
        fun(user)
        # run(user)







