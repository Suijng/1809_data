import os
import json

lists = []
dic = {}
while True:
    title = input('随便输入:')
    name = input('啥都行:')
    dic['title'] = title
    dic['name'] = name
    lists.append(dic)
    l = lists[1]
    print(l)

    f = open('suibian.json','a')
    f.write(json.dumps(l)+'\n')

