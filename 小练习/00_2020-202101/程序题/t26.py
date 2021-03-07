# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 11:32:16 2021

@author: 86159
"""

#26、编写函数，求任意整数的二进制形式中最后连续0的个数。

def f(n):
    x=bin(n)
    print(x)
    c=0
    print(x[:].rfind('0'))
    print(x[x.rfind('0')::-1])
    for i in x[x.rfind('0'):0:-1]:
        
        if i == '0':
            c+=1
        else:
            break
    return c
        

print(f(int(input('输入一个整数：'))))     

'''
def demo(n):
	b_n = bin(n)
	index = b_n.rfind('1') + 1
	return len(b_n[index:])


print(demo(int(input('输入一个整数：'))))     
'''