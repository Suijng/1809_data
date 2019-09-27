import re

strs = '''1. 理解:  * 除了正常运行模式(混杂模式),ES5添加了第二种运行模式："严格模式"（strict mode）。  * 顾名思义，这种模式使得Javascript在更严格的语法条件下运行2.目的/作用* 消除Javascript语法的一些不合理、不严谨之处，减少一些怪异行为* 消除代码运行的一些不安全之处，为代码的安全运行保驾护航* 为未来新版本的Javascript做好铺垫3.使用* 在全局或函数的第一条语句定义为: 'use strict';  * 如果浏览器不支持, 只解析为一条简单的语句, 没有任何副作用4.语法和行为改变* 必须用var声明变量	* 禁止自定义的函数中的this指向window	* 创建eval作用域'''

pattern = re.compile('.*?\.(.*?)\*')
result = re.findall(pattern, strs)
print(result)
