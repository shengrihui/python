# -*- coding: utf-8 -*-
"""
Created on Mon May  3 11:11:39 2021

@author: 11200
"""

import pandas as pd

df=pd.read_csv('人口.csv',encoding='gbk')
print(df.head())


print(df[['人口(万人)','面积(万平方千米)']][:5])

