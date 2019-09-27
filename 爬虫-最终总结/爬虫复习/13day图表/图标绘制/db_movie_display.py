# 豆瓣电影数据可视化

import requests
from lxml.html import etree
from pyecharts import Bar,Page
# 主题
from pyecharts.globals import ThemeType
from pyecharts import options as opts

## 电影名称 发布日期 类型 地区 关注量

url = 'https://movie.douban.com/cinema/later/beijing/'
response = requests.get(
    url=url,
    headers = {
        'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36'
    }
)


all_info = []
if response.status_code == 200:
    print('请求成功')
    etree_html = etree.HTML(response.text)
    # 提取电影信息
    alls = etree_html.xpath('//div[@class="bd"]/div[@id="showing-soon"]/div')
    for all in alls:
        info = {}
        # 名字
        info['name'] = all.xpath('.//h3/a/text()')[0]
        # 时间
        info['publishtime'] = all.xpath('.//div[@class="intro"]/ul/li[@class="dt"][1]/text()')[0]
        # 类型
        info['type'] = all.xpath('.//div[@class="intro"]/ul/li[@class="dt"][2]/text()')[0]
        # 地区
        info['area'] = all.xpath('.//div[@class="intro"]/ul/li[@class="dt"][3]/text()')[0]
        # 关注量
        info['attentionnum'] = all.xpath('.//ul/li[4]/span/text()')[0]

        all_info.append(info)

print(all_info)

### 根据电影名称和关注量绘制柱状图
bar = Bar(
    init_opts=opts.InitOpts(ThemeType.DARK)
)
# 以关注量作为x轴
attention_nums = [info['attentionnum'] for info in all_info]
# 以电影名作为y轴
names = [info['name'] for info in all_info]

# 添加x轴
bar.add_xaxis(attention_nums)
# 添加y轴
bar.add_yaxis('电影名称',names)

page = Page()

# 反转坐标
bar.reversal_axis()
bar.set_series_opts(
    table_opts=opts.TitleOpts(
        title='电影关注排行榜',
        position='right', #表示横向
    )
)

bar.set_global_opts(
    # 设置柱状的标题
    title_opts=opts.TitleOpts(
            title='电影关注排行榜',
        )
)

bar.render()
page.add(bar)
page.render()