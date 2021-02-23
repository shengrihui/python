# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def add(a):
    return a*2

class Person:
    province="浙江"
    city="玉环"
    count=0
    
    def __init__(self,name,age):
        self.name=name
        self.age=age
        Person.count+=1
    
    @classmethod
    def cityprint(cls,nm):
        print("这是类方法，{}地址在{}{}".format(nm,cls.province,cls.city))
        
    @staticmethod
    def fork(a,b):
        return abs(a-b)
    
    def say_age(self):
        print("这是实例方法，{}的年龄是{}".format(self.name,self.age))
    
    def __del__(self):
        print("{}的2被年龄是{}".format(self.name,add(self.age)))
        print("销毁{}".format(self.name))
        
p1=Person("盛日辉",21)
p2=Person("python",100)

p1.cityprint(p1.name)
print("一共有{}个person".format(Person.count))
p2.say_age()
Person.say_age(p1)
print("年龄差是{}".format(Person.fork(p1.age,p2.age)))

del p1
del p2

