# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 17:04:28 2020

@author: 86159
"""

'''
x=True
print(id(x))
y=True
print(id(y))
print(id(x)==id(y))
print(x is y)
'''

#不可变参数：数字、字符串、元组、布尔值
a=100
print('a',a,id(a))
def f(n):
    print('n',n,id(n))
    n+=123
    print('n',n,id(n))

f(a)
print('a',a,id(a))
    
print('*'*20)

a='srh'
print('a',a,id(a))
def f(n):
    print('n',n,id(n))
    n+='nb'
    print('n',n,id(n))

f(a)
print('a',a,id(a))