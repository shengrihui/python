# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 12:01:31 2021

@author: 86159
"""

#28、使用循环和列表推导式两种方法求解百钱买百鸡问题。假设大鸡5元一只，中鸡3元一只，小鸡1元三只，现有100元钱想买100只鸡，有多少种买法？


for x in range(21):
    for y in range(int((100-5*x)/3)+1):
        for z in range(int((100-5*x-3*y)*3)+1):
            if x+y+z==100 and 5*x+3*y+z/3 ==100 :
                print('大鸡%d只，中鸡%d只，小鸡%d只。' %(x,y,z))
                

li=[
    '大鸡%d只，中鸡%d只，小鸡%d只。' %(x,y,z)  
    for x in range(21) for y in range(34) for z in range(100-x-y+1) 
    if (x+y+z==100 and 5*x+3*y+z/3 ==100)
    ]

print(li)