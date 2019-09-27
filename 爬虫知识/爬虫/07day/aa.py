#coding=utf-8
import threading
import time

def saySorry():
    for i in range(5):
        print("亲爱的，我错了，我能吃饭了吗？",threading.current_thread().name)
        time.sleep(1)

def do():
    for i in range(5):
        print("亲爱的，我错了，我给你按摩",threading.current_thread().name)
        time.sleep(1)

if __name__ == "__main__":
    print(threading.current_thread().name,'主线程开始执行')

    td1 = threading.Thread(target=saySorry,name='线程一号')
    td1.start() #启动线程，即让线程开始执行
    td2 = threading.Thread(target=do,name='线程二号')
    td2.start() #启动线程，即让线程开始执行
    td1.join()
    td2.join()
    print(threading.current_thread().name, '主线程执行结束')