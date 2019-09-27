######re正则模块###########
"""
单字符匹配
.  匹配除了换行符之外的任意字符
\d 匹配数据0～9      => [0-9] => [^\D]
\D 匹配非数字  =>[^\d]
\s 匹配空白字符 空格 \n \r....
\S 匹配非空白字符
\w 匹配单词字符[a-zA-Z0-9_]
\W 匹配非单词字符 [^\w]
[a-z]
[1-34-9]

^ 匹配开头
$ 匹配结尾

多字符匹配（贪婪匹配）
*   匹配* 前的表达式任意次数
+   匹配+ 前的表达式至少1次
？   匹配？前的表达式0～1次
{n,m} 匹配{n,m} 前的表达式n~m次
{n} 匹配{n} 前的表达式n次

非贪婪匹配(竟可能少的匹配)
*？
+？
??

| 或
() 分组
r  原始字符
\  转义符
"""
import re

# re.compile():构建正则表达式对象
# re.match():从字符串起始位置匹配（第一个字符开始）,匹配到结果，立即返回,
#            否则，返回None，单次匹配
# re.search():从起始位置开始在整个字符串中匹配,匹配到结果，立即返回,
#             否则，返回None，单次匹配
# re.findall():匹配出字符串中所有符合正则表达式的结果，将匹配结果放入list中返回
# re.finditer():匹配出字符串中所有符合正则表达式的结果,返回的是一个可迭代对象
# re.split():根据正则表达式，分割字符串
# re.sub():根据正则表达式，替换字符串


#### get 请求##########
# http://top.hengyan.com/dianji/default.aspx?p=1
# http://top.hengyan.com/dianji/default.aspx?p=2

from urllib import request
import re

def get_rank_data(url='http://top.hengyan.com/dianji/default.aspx?p=1'):
    #构建请求头
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36',
    }
    # url, \目标url
    # data=None, \默认为None表示是get请求,如果不为None说明是get请求
    # timeout 设置请求的超时时间
    # cafile=None, capath=None, cadefault=False,:证书相关参数
    # context=None :忽略证书认证
    #urlopen不能添加请求头
    # response = request.urlopen(url=url,timeout=10)

    #添加请求头
    req = request.Request(url=url,headers=headers)
    response = request.urlopen(req,timeout=10)

    #响应状态码
    code = response.status
    #当前请求的url地址
    url = response.url
    print(code,url)

    b_content = response.read()
    # bytes -> str: decode
    # str -> bytes: encode
    # print(b_content)
    html = b_content.decode('utf-8')
    # print(html)
    # #文件操作
    # """
    # w:    w+:    wb:    wb+    a:    a+:    ab:    ab+:    r:    rb:
    # """
    # with open('hengyan.html','w') as file:
    #     file.write(html)

    #证据正则表达式解析数据
    # re.S 修饰：表示.可以匹配换行符

    pattern = re.compile('<div\sclass="list">(.*?)</div>',re.S)
    ul_str = re.findall(pattern,html)[0]

    pattern1 = re.compile('<ul.*?>(.*?)</ul>',re.S)
    li_strs = re.findall(pattern1,ul_str)[1:]

    for li_str in li_strs:
        # print(li_str)
        pattern = re.compile(
            '<li\sclass="num">(.*?)</li>'+
            '.*?<a.*?>(.*?)</a>'+
            '.*?<li.*?>(.*?)</li>'+
            '.*?<li.*?>(.*?)</li>'+
            '.*?<li.*?>(.*?)</li>'+
            '.*?<li.*?>(.*?)</li>',
            re.S
        )

        data = re.findall(pattern=pattern,string=li_str)[0]
        print(data)

    #提取下一页：
    if '下一页' in html:
        #说明还存在下一页
        pattern = re.compile('<span\sclass="pageBarCurrentStyle">(.*?)</span>',re.S)
        current_page = int(re.findall(pattern,html)[0])
        next_page = current_page+1
        #构造下一页的URL地址
        next_page_url = re.sub('\d+',str(next_page),url)
        print(next_page_url)
        get_rank_data(next_page_url)
    else:
        print('数据提取完毕')

if __name__ == '__main__':

    get_rank_data()