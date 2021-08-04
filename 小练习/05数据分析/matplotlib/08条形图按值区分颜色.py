# -*- coding: utf-8 -*-
"""
Created on Tue May  4 21:46:38 2021

@author: 11200
"""

from matplotlib import pyplot as plt
import numpy as np

x=range(10)
y=np.random.randint(-5,5,10)


v_bar=plt.bar(x,y)

#设置y=0的线
plt.axhline(0,color='orange',linewidth=2)
#plt.axvline(3)

for bar,height in zip(v_bar,y):
    if height<0:
        bar.set(color='red')


plt.show()

