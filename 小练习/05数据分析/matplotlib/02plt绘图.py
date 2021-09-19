# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 20:57:08 2021

@author: shengrihui
"""

from matplotlib import pyplot as plt
import random

import matplotlib

font = {'family': 'Microsoft YaHei',
        'weight': 'bold',
        'size': 12}
matplotlib.rc('font', **font)


# plt.rcParams['font.sans-serif'] = ['SimHei'] #解决中文显示
# plt.rcParams['axes.unicode_minus'] = False #解决符号无法显示


plt.figure(figsize=(16, 9), dpi=80)

# 十点到十二点每分钟得温度
a = [random.randint(20, 35) for i in range(120)]
b = range(120)


x_tick = list(b)
x_labels = ["{}时{}分".format(i//60+10, i % 60) for i in x_tick]
# 第一个参数刻度大小，第二个参数刻度显示内容
# rotation旋转角度
# matplotlib默认不支持显示中文
plt.xticks(x_tick[::3], x_labels[::3], rotation=45)


# 添加说明信息（x轴，y轴
plt.xlabel('时间')
plt.ylabel('温度')
plt.title('十点到十二点温度变化曲线')

plt.plot(b, a)

plt.savefig("02绘图.jpg")
plt.show()
