# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 23:10:20 2021

@author: shengrihui
"""

#单例模式

class MySingleten:
    
    __obj = None
    __init_flag = True
    
    def __new__(cls,*args,**kwargs):
        if cls.__obj == None:  #如果当前cls这个类的__obj属性为空，则创建新对象
            cls.__obj = object.__new__(cls)
        
        return cls.__obj

    def __init__(self,name):
        if MySingleten.__init_flag :
            self.name = name
            print("init ...",name)
            MySingleten.__init_flag = False 
  
a=MySingleten("python")
print(a,a.name)
b=MySingleten("spyder")
print(b,b.name)
