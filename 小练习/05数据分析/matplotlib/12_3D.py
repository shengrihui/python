# -*- coding: utf-8 -*-
"""
Created on Wed May  5 12:04:31 2021

@author: 11200
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

x=np.linspace(-10,10,100)
y=np.linspace(-10,10,100)
X,Y=np.meshgrid(x,y)

def Z(x,y):
    #return X**2+Y**2
    #return x+y
    return pow(x,3)*y+np.sin(y)*pow(x,2)

figure=plt.figure()

ax=Axes3D(figure)


ax.plot_surface(X,Y,Z(X,Y))

plt.show()