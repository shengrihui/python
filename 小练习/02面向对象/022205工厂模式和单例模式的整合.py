# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 23:36:01 2021

@author: shengrihui
"""

#工厂模式和单例模式的整合

class CarFactory:
    
    __obj=None
    __init_flag=True
    
    def __new__(cls,*args):
        if cls.__obj==None:
            cls.__obj=object.__new__(cls)
        return cls.__obj
    
    def __init__(self,name):
        if CarFactory.__init_flag :
            self.name=name
            print(name,"开厂了！")
            CarFactory.__init_flag=False
    
    def CreateCar(self,brand):
        if brand=="奔驰":
            print("已生产一辆奔驰")
            return Benz()
        elif brand=="宝马":
            print("已生产一辆宝马")
            return BMW()
        elif brand=="比亚迪":
            print("已生产一辆比亚迪")
            return BYD()
        else:
            print("本工厂造不了{}".format(brand))
        
class Benz:
    pass
class BMW:
    pass
class BYD:
    pass

cf=CarFactory("python")
print(cf)
cf2=CarFactory("spyder")
print(cf2)
cf2.CreateCar("奔驰")
