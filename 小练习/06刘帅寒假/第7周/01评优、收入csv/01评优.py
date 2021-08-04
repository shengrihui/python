# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 17:41:19 2021

@author: shengrihui
"""

userNames=["小明","李四","小明","李四",
           "李四","王五","李四","王五",
           "张三","李四","小明","李四",
           "张三","李四","王五","张三",
           "王五","幸福","张三","李四",
           "张三","李四",]

group_list=list(set(userNames))

result={}

for i in group_list:
    result[i]=result.get(i,0)+userNames.count(i)
    
result_list=list(result.items())
result_sort=sorted(result_list,key=lambda x:-x[1])

print(result_sort)
