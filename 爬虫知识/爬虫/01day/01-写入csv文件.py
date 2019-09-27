import csv
with open("1807.csv","w",encoding='utf-8-sig') as f:
    #创建文件语柄
    liebiao = csv.writer(f)
    #写入头部
    liebiao.writerow(["姓名","年龄","性别"])
    #单行写入
    liebiao.writerow(["小花","18","女"])
