# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 20:56:02 2021

@author: shengrihui
"""

fa=open(r"a.txt","w")
fa.write("盛日辉\n")
fa.close()


fa=open("a.txt","a")
strs=['aa\n','bb\n']
fa.writelines(strs)
fa.close()


with open("a.txt","r") as fa:
    print(fa.read())
with open("a.txt","r") as fa:
    print(fa.read(5))
with open("a.txt","r") as fa:
    print(fa.readline())
with open("a.txt","r") as fa:
    print(fa.readlines())
    
with open("b.txt","w",encoding="utf-8") as fb:
    with open("a.txt","r",encoding="gbk") as fa:
        lines=["{}  #{}\n".format(line.rstrip(),index+1) for index,line in enumerate(fa.readlines())]
    fb.writelines(lines)