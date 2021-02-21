# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


def maxCommonDivisor2(num1,num2):
    m=max(num1,num2)
    n=min(num1,num2)
    
    r=m-n
    while r !=0:
        m,n=max(n,r),min(n,r)
        r=m-n
    return m
    
if __name__ == '__main__':
    first=int(input('请输入第一个整数：'))
    second=int(input('请输入第二个整数：'))
    print('%d和%d的最大公约数是%d' %(first,second,maxCommonDivisor2(first,second)))
    
    