# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 21:38:08 2020

@author: 86159
"""

#8、编写函数，模拟Python内置函数sorted()。

def Sorted(v):
    t = v[::]
    r = []
    while t:
        tt = min(t)
        r.append(tt)
        t.remove(tt)
    return r


import random
x=[ random.randint(0,100) for i in range(10)]
print(x)
print(Sorted(x))

