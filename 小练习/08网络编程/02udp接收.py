# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 21:00:59 2021

@author: shengrihui
"""

from socket import *

udp_socket=socket(AF_INET,SOCK_DGRAM)

#绑定一个端口，本机 8989
udp_socket.bind(('10.160.149.141',8989))

addr=('10.160.45.54',10500)
#addr=('10.160.159.78',8080)
data=input('请输入：111111')
udp_socket.sendto(data.encode('gb2312'),addr)

#接收信息
#recvfrom方法，1024表示这次最多接收1024字节
recv_data=udp_socket.recvfrom(1024)
#元组的形式，第二个是来源主机，第一个是内容

#打印
print("接收到{}发来的信息：{}".format(recv_data[1],recv_data[0]))

udp_socket.close()



