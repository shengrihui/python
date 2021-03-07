# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import turtle
r=50
t=turtle.Pen()
t.width(3)
t.speed(5)
mcolor=("red","yellow","blue","black","green")
for i in range(15):
    t.penup()
    t.goto(0,-i*r)
    t.pendown()
    t.color(mcolor[i%len(mcolor)])
    t.circle(r+i*r)
t.done()