# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 23:04:06 2021

@author: shengrihui
"""

class Student():
    
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    def say_age(self):
        print("{0}的年龄是{1}".format(self.name,self.age))
        
s1=Student("盛日辉",18)
s1.say_age()