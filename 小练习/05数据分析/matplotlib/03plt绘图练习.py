# -*- coding: utf-8 -*-
"""
Created on Mon May  3 14:57:56 2021

@author: 11200
"""

from matplotlib import pyplot as plt
import random

plt.rcParams['font.sans-serif'] = ['SimHei'] #解决中文显示
plt.rcParams['axes.unicode_minus'] = False #解决符号无法显示

plt.figure(figsize=(16,9),dpi=80)

#自己的
age=list(range(11,31))
x_ticks=['{}岁'.format(i) for i in age]
num=[random.randint(0,5) for i in range(11,31)]

#同桌
num2=[random.randint(0,5) for i in range(11,31)]


#显示一些信息
plt.xlabel('年龄')
plt.ylabel('个数')
plt.title('不同年龄交男女朋友个数')

plt.xticks(age,x_ticks)
plt.yticks(num)

#添加网格，alpha设置透明度
#一个x和y对应一条线
plt.grid(alpha=0.6)


#绘图
plt.plot(age,num,label='自己',color='cyan')
plt.plot(age,num2,label='同桌',color='black')

#图例
plt.legend()

plt.savefig('03练习.png')
plt.show()



