# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 09:43:04 2021

@author: shengrihui
"""

import turtle as t

data_ls=[]
with open("data.txt","r") as f:
    lines=[]
    for line in f:
        line=line.strip('\n')
        line=line.split(',')
        line=list(map(eval,line))
        data_ls.append(line)
    
    
t.setup(800,600,300,400)
t.pensize(5)
t.color('red')
for i in data_ls:
    t.forward(i[0])
    t.color(i[3],i[4],i[5])
    if i[1]==1:
        t.right(i[2])
    elif i[1]==0:
        t.left(i[2])
    
    
t.done()        