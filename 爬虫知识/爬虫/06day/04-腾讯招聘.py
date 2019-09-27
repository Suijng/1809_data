import requests
import json
from bs4 import BeautifulSoup

def zhaopin(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
    }
    response = requests.get(url=url,headers=headers)
    html = response.content.decode('utf-8')
    content = BeautifulSoup(html)

    tr = content.select('.even')
    tr1 = content.select('.odd')
    da = tr+tr1
    for i in da:
        name = i.select('td a')[0].get_text()
        type = i.select('td')[1].get_text()
        renshu = i.select('td')[2].get_text()
        dizhi = i.select('td')[3].get_text()
        time = i.select('td')[4].get_text()

        data ={
            'name':name,
            'type':type,
            'renshu':renshu,
            'dizhi':dizhi,
            'time':time,
        }
        cunru(data)


def cunru(content):
    with open('zhaopin.json','a') as f:
        f.write(json.dumps(content,ensure_ascii=False)+'\n')



def main():
    start = int(input('输入起始页:'))
    end = int(input('请输入终止页:'))
    for i in range(start,end+1):
        url = 'https://hr.tencent.com/position.php?&start=' + str((i - 1)*10)
        zhaopin(url)


if __name__ == '__main__':
    main()