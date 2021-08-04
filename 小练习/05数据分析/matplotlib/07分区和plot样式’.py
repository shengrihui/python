# -*- coding: utf-8 -*-
"""
Created on Tue May  4 21:17:42 2021

@author: 11200
"""

from matplotlib import pyplot as plt
plt.figure(figsize=(100,100),dpi=100)

x=range(-100,101)
y=[i**2 for i in x]

styles=['--','-.',':','.','+','o','v','^','1','2','3','h','H','D','d','_']

print(len(styles))

def sub():
    for i in range(16):
        plt.subplot(4,4,i+1)
        plt.plot(x,y,styles[i])

def fun():
    for i in range(16):
        plt.plot([xi+i*2 for xi in x],y,styles[i])
        
#sub()
fun()
plt.savefig('07分区和不同样式.png')
plt.show()