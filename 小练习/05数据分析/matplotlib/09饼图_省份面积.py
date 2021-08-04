# -*- coding: utf-8 -*-
"""
Created on Wed May  5 10:45:51 2021

@author: 11200
"""

import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei'] #解决中文显示
df=pd.read_csv('人口.csv',encoding='gbk')

province=df['省份']
square=df['面积(万平方千米)']
s=sum(square)
perc=[i/s for i in square]

exp=tuple([0.15 for i in perc])


paches,texts=plt.pie(perc,labels=province,explode=exp,rotatelabels=True,
                     radius=1.2,)


plt.show()

