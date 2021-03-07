# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 21:25:56 2021

@author: shengrihui
"""

with open("c.png","rb") as fa:
    with open("c_copy.png","wb") as fb:
        s=fa.read()
        fb.write(s)
        print(fb.name)
        print(fb.mode)
        print(fb.closed)

print("完成1！")

with open("c.png","rb") as fa:
    with open("c_copy2.png","wb") as fb:
        #i=0
        for line in fa.readlines():
            fb.write(line)
            #i+=1
            # 10836
            #print(i)
print("完成2")

with open("c.png","rb") as fa:
    with open("c_copy3.png","wb") as fb:
        for line in fa.readlines()[:2345]:
            fb.write(line)
            
print("完成3")