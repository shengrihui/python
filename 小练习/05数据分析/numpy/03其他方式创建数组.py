# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 19:21:11 2021

@author: shengrihui
"""

import numpy as np

a=np.zeros(5)
print(a)
a2=np.zeros((3,4),dtype=np.int)
print(a2)

b=np.ones((3,2))
print(b)

c=np.empty((4,3))   #只是创建空间，不擦除内存上的数据
print(c)

print('\n等差数列')
d=np.linspace(0,10)
print(d)
d2=np.linspace(1,50,3)
print(d2)
d3=np.linspace(0, 50,3,False)
print(d3)
d4=np.linspace(100,0,20)
print(d4)

print("\n等比数列")
e=np.logspace(0,3,base=2)
print(e)
e2=np.logspace(3, -1,5,base=0.5)
print(e2)
