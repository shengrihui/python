# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 16:14:21 2020

@author: 86159
"""
'''
def maxCommonDivisor(num1,num2):
    m=max(num1,num2)
    n=min(num1,num2)
    r=m-n
    while r !=0:
        m,n=max(n,r),min(n,r)
        r=m-n
    return m
'''

#import maxCommonDivisor
from maxCommonDivisor import maxCommonDivisor2



def minCommonMultiple(num1, num2):
    m=maxCommonDivisor2(num1,num2)
    a,b=num1//m,num2//m
    return m*a*b

first=int(input('请输入第一个整数：'))
second=int(input('请输入第二个整数：'))
print('%d和%d的最小公倍数是%d' %(first,second,minCommonMultiple(first,second)))
