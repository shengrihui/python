# -*- coding: utf-8 -*-
"""
Created on Wed May  5 11:36:01 2021

@author: 11200
"""

import numpy as np
import matplotlib.pyplot as plt


#设置期望为0，方差为1.8的1000个正态分布的随机数
x=np.random.normal(0,1.2,1000)
#设置正态分布的随机数
y=np.random.randn(1000)
z=np.random.normal(-2,4,1000)

#bins表示多少个数据为一组
kwargs=dict(bins=100,alpha=0.3)

plt.hist(x,**kwargs)
plt.hist(y,**kwargs)
plt.hist(z,**kwargs)

plt.show()