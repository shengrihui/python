# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 20:04:39 2021

@author: shengrihui
"""

from socket import socket , AF_INET ,SOCK_DGRAM
#from socket import *

#创建udp套接字
udp_socket=socket(AF_INET,SOCK_DGRAM)

#接收键盘输入的要发送的消息
data=input("请输入：")

#创建接收信息的地址，元组形式
addr=('10.160.157.203',8080)

#调用sentto方法发送消息
udp_socket.sendto(data.encode('gb2312'), addr)
#网络助手默认的编码是gbk

#关闭套接字
udp_socket.close()



