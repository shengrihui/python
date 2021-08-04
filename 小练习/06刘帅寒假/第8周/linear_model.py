# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 16:47:58 2021

@author: shengrihui
"""

import matplotlib.pyplot as plt

from sklearn import linear_model

def show_linear_line(X_paremeters, Y_paremeters):
    regr = linear_model.LinearRegression()
    regr.fit(X_paremeters, Y_paremeters)
    plt.scatter(X_paremeters, Y_paremeters, color='blue')
    plt.plot(X_paremeters, regr.predict(X_paremeters), color='red',linewidth=4)
    #设置坐标轴的取值范围
    #plt.xlim(0,max(X_paremeters))
    plt.ylim(0,max(Y_paremeters)+1)
    
    plt.xticks() #x刻度
    plt.yticks() #y刻度
    
    #设置坐标轴的label
    plt.xlabel('M')  #震级
    plt.ylabel('T')  #频度
    
    plt.show()
    
    