# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 18:54:51 2021

@author: shengrihui
"""

#对象的浅拷贝和深拷贝
import copy
class MobilePhone:
    def __init__(self,cpu,screen):
        self.cpu=cpu
        self.screen=screen

class cpu:
    def __init__(self,name):
        self.name=name
    def acc(self):
        print("计算")

class screen:
    def show(self):
        print("show")
        
print("测试变量赋值")
c1=cpu("Kirin 9000")
c2=c1
c3=cpu("Kirin 9000")
print(c1.name,c1,c1.acc)
print(c2.name,c2,c2.acc)
print(c3.name,c3,c3.acc)


s1=screen()
s2=screen()
print(s1==s2)

#测试浅拷贝
print("测试浅拷贝")
m1=MobilePhone(c1,s1)
m2=copy.copy(m1)
print(m1,m1.cpu,m1.cpu.name)
print(m2,m2.cpu,m2.cpu.name)

#测试深拷贝
print("测试深拷贝")
m3=copy.deepcopy(m1)
print(m1,m1.cpu,m1.cpu.name)
print(m3,m3.cpu,m3.cpu.name)
print(m1.cpu.acc)
print(m2.cpu.acc)
print(m3.cpu.acc)



ss1="Kirin"
ss2="Kirin"
print(ss1==ss2)

