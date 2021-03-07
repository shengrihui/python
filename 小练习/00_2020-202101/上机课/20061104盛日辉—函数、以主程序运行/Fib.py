# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 16:30:28 2020

@author: 86159
"""

def Fib(num1):
    a,b=0,1
    for i in range(num1-1):
        print(a,end=',')
        a,b=b,a+b
    print(a)
        
num=int(input('请输入数列的长度（第一个数是0）：'))
Fib(num)