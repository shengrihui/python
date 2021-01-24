# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 16:56:26 2020

@author: 86159
"""

#可变参数（列表、字典、集合）

a=[10,20]

print(a)
print(id(a))
def test01(m):
    print(id(m))
    m.append(30)
    print(m)
test01(a)
print(a)

print('*'*25)

d={'a':1,'b':2}
print(id(d))
def test02(m):
    print(id(m))
    m.update(c=3)
    print(m)
test02(d)
print(d)
