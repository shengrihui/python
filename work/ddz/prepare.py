# -*- coding: utf-8 -*-
"""
Created on Sun Jan 10 18:55:02 2021

@author: shnegrihui
"""

import random
from sortp import *
pai_list=list('3456789')+['10']+list('JQKA2SB')
    
def fapai():
    p=list("A23456789JQK"*4)+['10']*4+['S','B']
    
    for i in range(100):
        random.shuffle(p)
    
    player1=[]
    player2=[]
    player3=[]
    while len(p)>3:
        player1.append(p.pop(0))
        player2.append(p.pop(0))
        player3.append(p.pop(0))
    
    
    return p,player1,player2,player3

if __name__=='__main__':
    t=fapai()
    for i in t:
        print(i)


