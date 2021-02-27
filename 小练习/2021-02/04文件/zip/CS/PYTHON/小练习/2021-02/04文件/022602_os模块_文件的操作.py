# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 09:07:43 2021

@author: shengrihui
"""

import os

'''
#1
os.system("notepad.exe")
os.system("cmd")
os.system("regedit")

os.startfile(r"D:\Program Files (x86)\Tencent\WeChat\WeChat.exe")

'''

'''
#2获取文件信息
print("操作系统的信息： ",os.name)      #windows  ->  nt ;linux , unix  -> posix
print("分隔符： ",os.sep)              #windows  ->  \ ;linux  -> /
print("换行符： ",repr(os.linesep))     #windows  ->  \r\n  ; linux  ->  \n
#repr() 函数将对象转化为供解释器读取的形式
#stat文件属性
#print(os.stat("022602_文件的操作.py"))
print(os.stat("a.txt"))
'''


'''
#3关于工作目录的操作
print(os.getcwd())  #获取当前工作目录   cwd current work dir
os.mkdir("书籍")      #创建新目录
os.chdir(os.getcwd()+"\书籍")
os.mkdir("python")
print(os.getcwd())
'''

'''
#4目录，多级目录
print(os.getcwd())
#os.rmdir("书籍\python")
#os.rmdir("书籍")
#os.makedirs(r"书籍\python\files")
#os.removedirs(r"书籍\python\files")
#os.rename("书籍","book")
#os.rename("022601csv.py","022601_csv.py")

dirs=os.listdir(os.getcwd())
#dirs=os.listdir("book")
print(dirs)


os.chdir("book\python")
os.mkdir("..\C")

'''
