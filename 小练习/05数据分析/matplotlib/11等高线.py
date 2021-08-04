# -*- coding: utf-8 -*-
"""
Created on Wed May  5 11:54:43 2021

@author: 11200
"""

import numpy as np
from matplotlib import pyplot as plt

#设置x,y的值
x=np.linspace(-10,10,100)
y=np.linspace(-10,10,100)

#计算x,y的交点
X,Y=np.meshgrid(x,y)

#z值
Z=np.sqrt(X**2+Y**2)
#print(X,Y,Z)
plt.contour(X,Y,Z)
plt.show()
plt.contourf(X,Y,Z)
plt.show()


