# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 12:00:31 2021

@author: shengrihui
"""

from sortp import *

def err(pai,pl):
    pll=pl[:]
    #判断飞机或者联队的部分是否正确
    def pp(lp,lc,n):
        for i in range(1,len(lp)):
            if  lc[i]==n:
                if sort_v(lp[i]) != sort_v(lp[i-1])-1:
                    return False
        else :
            return True
    #如果出的牌不在玩家的牌当中
    for i in pai:
        try:
            pll.remove(i)
        except:
            return False
    lp=count_pai(pai)[0]
    lc=count_pai(pai)[1]
    cm=max(lc)
    for i in lc:
        if i>4:
            return False
    if pai.count('S')>1 or pai.count('B')>1:
        return False
    if cm==4 :
        if len(lp)!=1:
            return False
    elif cm==3 :
        if lc.count(3)!=(lc.count(2) or lc.count(1)) :
            return False
        return pp(lp,lc,cm)
    elif cm==2:
        if len(lp)==2 or (1 in lc):
            return False
        return pp(lp,lc,cm)
    elif cm ==1:
        if len(lp)==1:
            return True
        if len(lp)<5 :
            if 'S' not in lp and 'B' not in lp:
                return False
        return pp(lp,lc,cm)
    else:
        return True
    
    
    
if __name__=='__main__':
    for i in range(10):
        t=input('出牌:')
        t=t.strip(' ')
        t=t.upper()
        tt=t.split(' ')
        print(err(tt))
        if err(tt):
            print(sort_pai_c(tt))
            print(pai_type(tt))
    