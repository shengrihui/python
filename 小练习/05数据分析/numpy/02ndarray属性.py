# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 20:32:33 2021

@author: shengrihui
"""

import numpy as np

a=np.arange(9)
b=np.array([[1,2,3],[5,4,6]],dtype='int64')
c=np.random.random(size=(2,3,5))

print(a);print(b);print(c)

print('多少维度ndim:',a.ndim,b.ndim,c.ndim)
print('总元素个数size:',a.size,b.size,c.size)
print('维度shape:',a.shape,b.shape,c.shape)
print('元素类型dtype:',a.dtype,b.dtype,c.dtype)
print('每个元素大小itemsize:',a.itemsize,b.itemsize,c.itemsize)

print()
#print('对象内存信息flags',a.flags,b.flags,c.flags)
#print('元素实部real:',a.real,b.real,c.real)
#print('元素虚部imag:',a.imag,b.imag,c.imag)

