#### get 请求##########
# http://top.hengyan.com/dianji/default.aspx?p=1
# http://top.hengyan.com/dianji/default.aspx?p=2

from urllib import request

url = 'http://top.hengyan.com/dianji/default.aspx?p=1'
#构建请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
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
#文件操作
"""
w:    w+:    wb:    wb+    a:    a+:    ab:    ab+:    r:    rb:
"""
with open('hengyan.html','w') as file:
    file.write(html)


###############post请求###########
from urllib import parse,error
import json

def get_ssjy_data(page=1,timout=10):
    # 世纪佳缘网
    url = 'http://search.jiayuan.com/v2/search_v2.php'
    # 请求参数
    """
    sex: f
    key: 
    stc: 1:11,2:20.28,23:1
    sn: default
    sv: 1
    p: 1 (页码)
    f: search
    listStyle: bigPhoto
    pri_uid: 0
    jsversion: v5
    
    """

    #构建请求头
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
    }
    #post请求参数
    form_data={
        'sex': 'f','key':'','stc': '1:11,2:20.28,23:1',
        'sn': 'default','sv': '1','p': str(page),
        'f': 'search','listStyle': 'bigPhoto',
        'pri_uid': '0','jsversion': 'v5',
    }

    form_data = parse.urlencode(form_data).encode('utf-8')
    print(form_data)
    #b'sex=f&key=&stc=1%3A11%2C2%3A20.28%2C23%3A1&sn=default&sv=1&p=1&f=search&listStyle=bigPhoto&pri_uid=0&jsversion=v5'
    #构建请求对象
    req = request.Request(url=url,data=form_data,headers=headers)

    try:
        response = request.urlopen(req,timeout=timout)

        if response.status == 200:
            content = response.read().decode('utf-8').replace('##jiayser##//', '').replace('##jiayser##', '')
            # print(content)
            # json.load():将本地文件中json字符串，转换成python数据类型（dict)
            # json.loads():将json字符串，转换成python数据类型（dict）
            # json.dump():将python数据类型转为json字符串，并且保存至本地文件
            # json.dumps():将python数据类型转为json字符串
            data = json.loads(content)
            print(type(data))
            # print(data)
            userinfos = data['userInfo']

            for user in userinfos:
                age = user['age']
                name = user['nickname']
                gender = user['sex']
                print(age, name, gender)

            # 获取下一页
            total_page = int(data['pageTotal'])
            print(str(page) + '页数据提取完毕')
            if page < total_page:
                # 需要继续提取下一页
                next_page = page + 1
                # 递归的方式，继续提取下一页数据
                get_ssjy_data(page=next_page)
            else:
                # 数据提取完毕
                print('数据提取完毕')
    except error.HTTPError as err:
        print(err.code)
        print(err.reason)
        print(err.headers)
        ####重新在次发起请求
        get_ssjy_data(page,timout=10)
    except error.URLError as err:
        print(err.reason)


######################证书错误##############
import ssl

url = 'https://www.baidu.com/'
#忽略证书认证
context = ssl._create_unverified_context()
response = request.urlopen(url=url,context=context)

if response.status == 200:
    print('百度请求成功')



#########使用urllib请求添加代理##############

url = 'http://www.baidu.com/'

proxy = {
    'http':'192.168.1.22:8000',
    'https':'192.168.1.33:8080',
}
#创建代理的处理器
proxy_handler = request.ProxyHandler(proxies=proxy)

#自定义opener
opener = request.build_opener(proxy_handler)

#构建请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36',
}
req = request.Request(url=url,headers=headers)
response = opener.open(req)
print(response.code)

# if __name__ == '__main__':
#     get_ssjy_data()