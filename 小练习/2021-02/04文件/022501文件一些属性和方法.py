# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 15:12:32 2021

@author: shengrihui
"""

#tell seek  truncate
str1=['盛日辉 b\n','aaaaaaaaaaaaaaaaaaaaa\n','abcd\n']
with open("d.txt","w",encoding="utf-8") as fd:
    fd.writelines(str1)
    print(fd.name,fd.mode,fd.closed)

print(fd.closed)

with open("d.txt","rb+") as fd:
    print(fd.tell())
    fd.seek(3)
    print(fd.readline())
    
    print(fd.tell())
    fd.seek(-7,1)
    print(fd.readline())
    
    fd.truncate(4)
    fd.seek(0,0)
    print(fd.readlines())
    