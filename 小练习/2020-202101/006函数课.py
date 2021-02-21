# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 15:12:36 2020

@author: 86159
"""

def fact(n,m=5):
    s=1
    for i in range(1,n+1):
        s*=i
    return s//m

print(fact(m=5,n=2))



i=5
def fun(arg=i):
    print('arg',arg)

i=55
fun(35)


print('xyz'*5)
def fun4(c,x=1,y=2,z=3):
    print(x**3+\
          y**2+z+c)

fun4(y=5,z=3,c=5)
