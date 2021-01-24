# -*- coding: utf-8 -*-
"""
Created on Fri Dec 25 19:30:44 2020

@author: 86159
"""

f=lambda x : 1 if x>0 else (-1 if x<0 else 0)
print(f(int(input('input a number:'))))

import math
def g(x):
    return math.cos(x)
print(g(0))

def h(x):
    return pow(x,2)
y=h(g(0))
print(y)


print(pip list)