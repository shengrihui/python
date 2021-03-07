# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 10:21:28 2021

@author: shengrihui
"""

import time

a=int(input("a="))
b=int(input("b="))
m=a if a<=b else b
ts=time.time()
for i in range(m,0,-1):
    if a%i==0 and b%i==0 :
        print("结果是：%d" %i)
        break
te=time.time()
t1=te-ts
print(t1)

ts=time.time()
for i in range(m,0,-1):
    if a%i==0:
        if b%i==0:
            print("结果是：%d" %i)
            break
te=time.time()
t2=te-ts
print(t2)



def maxCommonDivisor2(num1,num2):
    m=max(num1,num2)
    n=min(num1,num2)
    
    r=m-n
    while r !=0:
        m,n=max(n,r),min(n,r)
        r=m-n
    return m
ts=time.time()
print("结果是：%d" %maxCommonDivisor2(a,b))
te=time.time()
t3=te-ts
print(t3)




def maxCommonDivisor(num1,num2):
    m = max(num1,num2)
    n = min(num1,num2)
    r = m % n
    while r != 0:
        m,n =n,r
        r = m % n
    return n
ts=time.time()
print("结果是：%d" %maxCommonDivisor(a,b))
te=time.time()
t4=te-ts
print(t4)



print(list(sorted([(t1,'t1'),(t2,'t2'),(t3,'t3'),(t4,'t4')])))
