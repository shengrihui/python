# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 15:55:04 2021

@author: shengrihui
"""

#方法重写

class Person:
    
    def work(self):
        print("好好学习")
    
def play(s):
    print("玩游戏")
  
def work2(a):
    print("good good study")


p1=Person()

p1.work()

Person.play=play
p1.play() #-->Person.play(p1)

Person.work=work2
p1.work()

