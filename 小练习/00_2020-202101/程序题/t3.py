# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 20:52:52 2020

@author: 86159
"""


#3、编写程序，生成一个包含20个随机整数的列表，然后对其中偶数下标的元素进行降序排列，奇数下标的元素不变。（提示：使用切片。）

import random

li=[ random.randint(0,100) for i in range(20)]

print(li)
x=li[::2]
x.sort(reverse=True)
li[::2]=x
print(li)



