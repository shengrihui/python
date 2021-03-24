# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 23:42:56 2021

@author: shengrihui
"""

from turn_mode import *


record=[]
unfinished=[
    ['yello','yellow','yellow','yellow'],
    ['red','red','red','red'],
    ['green','green','green','green'],
    ['orange','orange','orange','orange'],
    ['blue','blue','blue','blue'],
    ['white','white','white','white']  
    ]

finished=[
    ['yello','yellow','yellow','yellow'],
    ['red','red','red','red'],
    ['green','green','green','green'],
    ['orange','orange','orange','orange'],
    ['blue','blue','blue','blue'],
    ['white','white','white','white']  
    ]


def go(unfinished,record):
    unfinished,record=right(unfinished,record,1)

go(unfinished,record)
print(unfinished)
print(record)