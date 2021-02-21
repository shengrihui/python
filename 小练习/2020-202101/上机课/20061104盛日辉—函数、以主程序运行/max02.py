# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 16:36:58 2020

@author: 86159
"""

def maxCommonDivisor(num1,num2):
    m = max(num1,num2)
    n = min(num1,num2)
    r = m % n
    while r != 0:
        m,n =n,r
        r = m % n
    return n


first=int(input('请输入第一个整数：'))
second=int(input('请输入第二个整数：'))
print('%d和%d的最大公约数是%d' %(first,second,maxCommonDivisor(first,second)))