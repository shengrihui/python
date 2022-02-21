# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 22:13:50 2021

@author: shengrihui
"""

import os

path=os.getcwd()


for i in os.walk(path):
    print(i[1:])

print()

for dirpath,dirnames,filenames in os.walk(path):
    print("{}  里\n文件夹有：".format(dirpath))
    for dirname in dirnames:
        print(dirname,end="\t")
    print("\n文件有：")
    for filename in filenames:
        print(filename,end="\t")
    print()

print()

d=0;f=0
for dirpath,dirnames,filenames in os.walk("E:/"):
    for dirname in dirnames:
        #print(os.path.join(dirpath,dirname))
        d+=1
    for filename in filenames:
        #print(os.path.join(dirpath,filename))
        f+=1
print("E盘一共有{}个文件夹，{}个文件。".format(d,f))
