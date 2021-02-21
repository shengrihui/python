# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 21:03:39 2020

@author: 86159
"""

#7、编写函数，判断一个数字是否为素数，是则返回字符串YES，否则返回字符串NO。
import math
def f(n):
    for i in range(2,int(math.sqrt(n)+1)):
        if n%i==0:
            return 'Yes'
            break
    else:
        return 'No'


print(f(int(input('请输入一个整数：'))))
