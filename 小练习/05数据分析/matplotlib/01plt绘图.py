# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 20:13:34 2021

@author: shengrihui
"""

from matplotlib import pyplot as plt

#调整图片大小
#figure是图形图像得意思，figsize元组宽高，dpi表示每英寸上像素个数，即清晰度
plt.figure( figsize=(20,15) ,dpi=80 )


#x,y长度应该一样
x=range(8)
y=[2,3,4,8,12,2,8,5]

plt.plot(x,y)

#设置x得刻度
#显示什么传什么，坐标不在范围内得不显示刻度
plt.xticks(range(15))
plt.yticks(range(min(y),max(y)+1))



#保存
plt.savefig('01plt绘图.png')

plt.show()