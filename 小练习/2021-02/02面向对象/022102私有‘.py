# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 15:36:14 2021

@author: shengrihui
"""

#私有属性
#私有方法

class Employee:
    
    __company="bbb"
    
    def __init__(self,name,age):
        self.name=name
        self.__age=age
    
    def __call__(self,s):  #s是一个月的salary
        print("发工资")
        ys=s*12
        ds=s//22.5
        hs=ds//8
        return dict(年薪=ys,月薪=s,日新=ds,时薪=hs)
    
    def __work(self):
        print("hello,age=%d" %(self.__age))
        
e=Employee("盛日辉",10)
print(e.name)
#print(e.age)
print(e._Employee__age)
print(dir(Employee))
print(dir(e))

e._Employee__work()
print(Employee._Employee__company )

print()
print(e(5000))
