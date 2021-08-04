# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 14:24:50 2021

@author: shengrihui
"""

#多态
#super()
#isinstance

class Man:
    def eat(self):
        print("吃饭啦")

class Chinese(Man):
    def eat(self):
        super().eat()
        print("用筷子")

class English():
    def eat(self):
        print("用刀叉吃饭")

class Zhejiang(Chinese):
    def eat(self):
        #super().eat()
        print("浙江菜")

def maneat(m):
    if isinstance(m,Man):
        m.eat()
    else:
        print("不能吃饭")
        
maneat(Chinese())
maneat(Zhejiang())
maneat(English())