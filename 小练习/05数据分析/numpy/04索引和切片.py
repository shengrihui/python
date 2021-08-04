# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 21:50:13 2021

@author: shengrihui
"""

import numpy as np

#一维数组的索引和切片和列表的索引切片一样一样一样

#二维数组
a=np.arange(12)
a=a.reshape((4,3))
print(a)

print(a[::2,::2])

print(a[3,2])

print(a[(0,0),[1,2]]) #返回的是a[0,1],a[0,2]
print(np.array([a[0,1],a[0][2]]))