# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 11:40:28 2021

@author: shengrihui
"""

import csv

data_ls={}
with open("收入数据.csv",'r',encoding='gbk') as f:
    ls=list(csv.reader(f))



for m,i in ls[1:]:
    m=m.split('-')
    m=int(m[1])
    data_ls[m]=data_ls.get(m,0)+int(i)

data=[(m,i) for m,i in data_ls.items()]
for i in data:
    print(i)


