# -*- coding: utf-8 -*-
"""
Created on Mon May  3 10:02:09 2021

@author: 11200
"""

import pandas as pd

df=pd.read_csv('人口.csv',encoding='gbk')
print(df)


#打印前几个，默认前5个
print('\nhead()\n',df.head(8))

print('\ninfo()\n')
df.info()

#索引
print('\nindex\n',df.index)

#列名
print('\ncolumns\n',df.columns)

#类型
print('\dtypes\nn',df.dtypes)

#每一行的值，数据类型是numpy的ndarray
print('\nvalues\n',df.values)
print(type(df.values))


#取某一列的值，类型是Series
population=df['人口(万人)']     #如果出现Nan表示里缺少值
print(population[::5])
print(type(population))
print('\n',population.index)
print('\n',population.values[:6])


print('\n\n换索引')
print(df[4:12])
df=df.set_index("省份")
print(df.head())
population=df['人口(万人)']
print(population[::5])



print('\n\n对一列数据进行运算\n')
print('min(population',min(population))
print('population.max()',population.max())

#对数据进行简单的统计分析，
#有多少数据，平均值，标准差等
print(df.describe())

population+=500000000
print(population[:5])


'''


print('\n\n\n\n\n----------------自己创建DataFrame--------------')

data={'coutry':['aaa','bbb','ccc'],
      'population':[11,23,32]
      }
my_df=pd.DataFrame(data)
print(my_df)
my_df.info()
'''