# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 14:54:33 2020

@author: 86159
"""

f= lambda a,b,c:a+b+c
print(f)
print(f(1,2,3))

g=[lambda a:a*2,lambda b:b*100]
print(g[0](12) )
