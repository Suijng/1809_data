import urllib.request
import urllib.parse

# url = "https://www.baidu.com/s?wd=%E9%9A%8B%E5%A9%A7&pn=0"


# 加载每页数据
def jiazai(url, filename):
    print("正在下载" + filename)
    response = urllib.request.urlopen(url=url)
    content = response.read().decode()
    xieru(content, filename)


# 写入每页数据
def xieru(content, filename):
    print("正在写入" + filename)
    with open("suijing/" + filename, "w") as f:
        f.write(content)


def main():
    wd = input("请输入要要爬的数据")
    start = int(input("请输入起始页"))
    end = int(input("请输入终止页"))
    for i in range(start, end + 1):
        url = "http://www.baidu.com/s?" + urllib.parse.urlencode({"wd": wd, "pn": (i - 1) * 10})
        # print(url)
        filename = "第" + str(i) + "页.html"
        jiazai(url, filename)


if __name__ == "__main__":
    main()
