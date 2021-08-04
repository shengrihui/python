# -*- coding: utf-8 -*-
"""
Created on Tue May  4 14:01:10 2021

@author: 11200
"""

import pandas as pd
from matplotlib import pyplot as plt

#中文字体和设置图片
plt.rcParams['font.sans-serif'] = ['SimHei'] #解决中文显示
plt.rcParams['axes.unicode_minus'] = False #解决符号无法显示
plt.figure(figsize=(16,9),dpi=80)

#获取数据
df=pd.read_csv('人口.csv',encoding='gbk')
province_list=list(df['省份'])
population_list=list(df['人口(万人)'])
square_list=list(df['面积(万平方千米)'])



def plt_bar():
    plt.bar(range(len(province_list)),population_list,width=0.4,color='green',label='人口(万人)')
    plt.bar([ i+0.4 for i in range(len(province_list))],square_list,width=0.4,color='blue',label='面积(万平方千米)')
    
    plt.xticks(range(len(province_list)),province_list)
    plt.grid(alpha=0.6)
    plt.legend()

def plt_barh():
    plt.barh(range(len(province_list)),population_list,height=0.4,color='green',label='人口(万人)')
    plt.barh([ i+0.3 for i in range(len(province_list))],square_list,height=0.4,color='blue',label='面积(万平方千米)')
    
    plt.yticks(range(len(province_list)),province_list)
    plt.grid(alpha=0.6)
    plt.legend()
  
#plt_bar()
plt_barh()

plt.savefig('05条形图_人口.png')
plt.show()
