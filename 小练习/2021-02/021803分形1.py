# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 23:34:02 2021

@author: shengrihui
"""

import turtle
import math

t=turtle.Pen()
t.speed(0)
def draw(x1,y1,x2,y2,x3,y3,n):
    x4,y4=(x1+x2)/2,(y1+y2)/2
    x5,y5=(x2+x3)/2,(y2+y3)/2
    x6,y6=(x3+x1)/2,(y3+y1)/2
    
    t.penup()
    t.goto(x4,y4)
    t.pendown()
    t.goto(x5,y5)
    t.goto(x6,y6)
    t.goto(x4,y4)
    
    if n>1:
        draw(x1,y1,x4,y4,x6,y6,n-1)
        draw(x4,y4,x2,y2,x5,y5,n-1)
        draw(x6,y6,x5,y5,x3,y3,n-1)
        
r=50

x1,y1=-r*math.sqrt(r),-r
x2,y2=r*math.sqrt(r),-r
x3,y3=0,r*math.sqrt(r)

t.penup()
t.goto(x1,y1)
t.pendown()
t.goto(x2,y2)
t.goto(x3,y3)
t.goto(x1,y1)

n=6
draw(x1,y1,x2,y2,x3,y3,n)

t.done()