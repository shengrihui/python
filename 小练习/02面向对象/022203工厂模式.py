# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 20:36:27 2021

@author: shengrihui
"""

#工厂模式

class CarFactory:
    
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

cf=CarFactory()
c1=cf.CreateCar("奔驰")
c11=cf.CreateCar("奔驰")

c2=cf.CreateCar("宝马")
c3=cf.CreateCar("比亚迪")
c4=cf.CreateCar("丰田")
print(c1)
print(c11)
print(c2)
print(c3)
print(c4)
