# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 18:51:35 2021

@author: shengrihui
"""

import os
import os.path as op

path=os.getcwd()
print(path)
print('1',op.isabs("E:/CSTS"))  #True
print('2',op.isdir("E:\c"))     #False
print('3',op.isdir("E:\CSTS"))  #True
print('4',op.isfile("b.txt"))   #True
print('5',op.isfile(path+"\b.txt")) #False
print('6',op.isfile(path+"/b.txt")) #True
print('7',op.isfile("E:/a.txt"))    #True
print('8',op.exists(path+'/cc.txt'))    #False

print('###################')
print(op.getsize(path))
print(op.getsize('b.txt'))
print(op.abspath('b.txt'))
print(op.dirname(path+"/b.txt"))
print(op.getatime('b.txt')) #访问时间
print(op.getctime('b.txt')) #创建时间
print(op.getmtime('b.txt')) #最后访问时间

print('################')
path2=op.abspath('b.txt')
print(path2)
print(op.split(path2))
print(op.splitext(path2))  #文件扩展名

print(op.join('aa','bb','xc'))


files_list2=[names for  names in os.listdir(os.getcwd()) if names.endswith("py")]
print(files_list2)