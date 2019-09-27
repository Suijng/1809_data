import socket

def service_client():
    """为这个客户端返回数据"""
    # 接收浏览器发送过来的请求,即http请求
    # GET / HTTP/1.1
    request = new_socket.recv(1024)
    print(request)


def main():
    """用来完成整体的控制"""
    # 1.创建套接字
    tcp_server_socke = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # 2.绑定
    tcp_server_socke.bind(("",7890))
    # 3.变为监听套接字
    tcp_server_socke.listen(128)
    # 4.等待新客户端的链接


if __name__ == '__main__':
    pass


'''
# 三次挥手
1.是客户端告诉服务器要准备好资源
2.是服务器告诉客户端,我已经准备好了,你准备好了么
3.我也准备好了

# 四次握手
1.客户端告诉服务器不会在给服务器发送任何数据了
2.收到了
'''