# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 12:33:56 2021

@author: shengrihui
"""

#@property

class Employee1:
    
    def __init__(self,name,age,salary):
        '''私有属性，封装'''
        self.__name=name
        self.age=age
        self.__salary=salary
        
    def get_salary(self):
        return self.__salary

print("直接访问对象的属性值，可以修改，但用户可能输入错误的数")
emp1=Employee1("srh",18,10000)
print("emp1.age:",emp1.age)
emp1.age=200
print("emp1.age:",emp1.age)

print("get_salary访问私有属性，但不能修改")    
print("emp1.get_salary():",emp1.get_salary())



'''用get和set'''
class Employee2:
    
    def __init__(self,name,salary):
        self.name=name
        self.__salary=salary
    
    def get_salary(self):
        return self.__salary
    
    def set_salary(self,salary):
        if 0<salary<10000:
            self.__salary=salary
        else:
            print("输入范围应为0到10000")

print()
print("用get_salary和set_salary")
emp2=Employee2("srh",1000)
print("emp2.get_salary():",emp2.get_salary())
emp2.set_salary(5000)
print("emp2.get_salary():",emp2.get_salary())
emp2.set_salary(-5000)
print("emp2.get_salary():",emp2.get_salary())



'''用@property'''
class Employee3:
    
    def __init__(self,name,salary):
        self.__name=name
        self.__salary=salary
        
    @property
    def salary(self):
        return self.__salary
    
    @salary.setter
    def salary(self,salary):
        if 0<salary<10000:
            self.__salary=salary
        else:
            print("输入范围应为0到10000")
        
print()
print("使用@proprety")
emp3=Employee3("srh",100)
print("emp3.salary:",emp3.salary)
'''当作属性直接赋值'''
emp3.salary=9999
print("emp3.salary:",emp3.salary)
emp3.salary=99999
print("emp3.salary:",emp3.salary)





