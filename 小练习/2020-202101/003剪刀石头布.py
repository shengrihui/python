# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 23:05:12 2020

@author: 86159
"""

import random
print("1-剪刀，2-石头，3-布，4-退出")
t=int(input("输入："))
act=["","剪刀","石头","布"]
result=["你赢了！","你输了！","平局！"]
while t<4:
    comp=random.randint(1,3)
    if abs(t-comp)==1:
        if t>comp:
            re=0
        else :
            re=1
    elif t==comp:
        re=2
    else:
        if t==1 :
            re=0
        else:
            re=1
    print("你出的是%s，电脑出地是%s，结果是%s" %(act[t],act[comp],result[re]))
    t=int(input("输入："))
print("游戏结束！")
