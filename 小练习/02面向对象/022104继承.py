# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 19:55:51 2021

@author: shengrihui
"""

#继承
#多重继承

class Person:
    
    def __init__(self,name,age):
        self.name=name
        self.__age=age
        
    def say_age(self):
        print("不告诉你我几岁了。")
        
class Student(Person):
    
    def __init__(self,name,age,score):
        Person.__init__(self,name,age)
        self.score=score
    
    def say_age(self):
        '''方法重写'''
        print("我的年龄是100岁。")

s1=Student("盛日辉",18,60)

s1.say_age()
print(s1.name)
print(s1._Person__age)



class A:
    def aa(self):
        print("aaa")
class B(A):
    def bb(self):
        print("bbb")
class C(A):
    def bb(self):
        print("ccc")
class D(C,B):
    def dd(self):
        print("ddd")
print()
d=D()
d.bb()
print(dir(d))
print(D.__mro__)