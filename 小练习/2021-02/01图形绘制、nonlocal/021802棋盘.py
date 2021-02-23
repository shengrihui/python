# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import turtle

t=turtle.Pen()
t.speed(10)
r=25
c=18
l=r*c
for i in range(c+1):
    t.penup()
    t.goto(-l/2+i*r,l/2)
    t.pendown()
    t.goto(-l/2+i*r,-l/2)
    
    t.penup()
    t.goto(-l/2,-l/2+i*r)
    t.down()
    t.goto(l/2,-l/2+i*r)
    
t.done()