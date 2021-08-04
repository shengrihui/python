# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 18:05:37 2021

@author: shengrihui
"""


from sortp import *

def pai_type(pai):
    lp=count_pai(pai)[0]
    lc=count_pai(pai)[1]
    le=len(lp)
    cm=max(lc)
    '''
    cm  牌出现的最多次数
    '''
    if lc==[4]:
        return "炸弹"
    elif cm==3 :
        #次数3出现的次数，用于判断是几个飞机
        c3=lc.count(3)
        if c3==1:
            if lc==[3]:
                return '三个'
            elif lc==[3,1]:
                return '三带一'
            elif lc==[3,2]:
                return '三带二'
        elif c3>1:
            return '飞机{}'.format(c3)
    elif cm==2:
        if le==1:
            return '一对'
        elif le>2 :
            return '连对{}'.format(le)
    elif cm==1:
        if le==1:
            return '一张'
        elif le>=5 :
            return '顺子{}'.format(le)
        elif le==2 :
            if lp==['B','S']:
                return '王炸'
            
            
                        
if __name__=='__main__':
    for i in range(3):
        t=input('出牌:')
        t=t.strip(' ')
        t=t.upper()
        tt=t.split(' ')
        print(err(tt))
        print(sort_pai_c(tt))
        print(pai_type(tt))
    