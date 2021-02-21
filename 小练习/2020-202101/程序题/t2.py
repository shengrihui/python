# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 17:08:55 2020

@author: 86159
"""



import time


a=time.time()
x = list(range(500))
for item in x:
    t = 5**5
    print(item+t)
b=time.time()
t1=b-a

a=time.time()
x = list(range(500))
t = 5**5
for item in x:
    print(item+t)
b=time.time()
t2=b-a

print(t1)
print(t2)
print('t1<t2' if t1<t2 else 't1>t2')





