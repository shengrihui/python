# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 21:43:57 2020

@author: 86159
"""




#9、编写程序，生成包含20个随机数的列表，然后将前10个元素升序排列，后10个元素降序排列，并输出结果。


import random
x=[ random.randint(0,100)  for i in range(20)]

print(x)

a=x[:10]
b=x[10:]
a.sort()
b.sort(reverse=True)

x=a+b
print(x)




