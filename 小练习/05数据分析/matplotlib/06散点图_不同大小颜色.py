# -*- coding: utf-8 -*-
"""
Created on Tue May  4 20:12:00 2021

@author: 11200
"""

from matplotlib import pyplot as plt
import numpy as np

np.random.seed(0)
x=np.random.rand(100)
y=np.random.rand(100)

size=np.random.rand(100)*1000
color=np.random.rand(100)

plt.scatter(x,y,s=size,c=color,alpha=0.7)


plt.show()
