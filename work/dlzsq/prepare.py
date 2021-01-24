# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 10:46:05 2020

@author: 86159
"""

ch=[]
chp={}
x=list(range(-5,6))*11
y=[i for i in range(5,-6,-1) for j in range(11)]
chessperk=list(zip(x,y))

chessperva=[1 if (abs(a)<=1 and abs(b)<=3) or (abs(b)<=1 and abs(a)<=3) else 0  for a,b in zip(x,y)  ]
chesspervb=[False]*len(chessperva)
chessperv=list(zip(chessperva,chesspervb))
chessper={
        k:v
        for k in chessperk
        for v in chessperv
        }
chessper[(0,0)]=[-1,True]


'''
z=list(chessper.items())
for i in range(11):
    print(chessperva[i*11:i*11+11])

print()
print(chessper)

    '''

