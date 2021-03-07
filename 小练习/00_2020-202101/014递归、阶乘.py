# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 15:27:00 2020

@author: 86159
"""

def f(n):
    print('test',n)
    if n==0:
        print('over')
    else:
        f(n-1)
    print('****',n)
    
f(4)

print('*'*20)
for i in range(4,-1,-1):
    print('test',i)
    if i==0:
        print('over')
else:
    for i in range(5):
        print('***',i)

print('*'*20)

def jiecheng(n):
    if n>1:
        return jiecheng(n-1)*n
    else:
        return 1
print(jiecheng(3))

