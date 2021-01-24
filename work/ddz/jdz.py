# -*- coding: utf-8 -*-
"""
Created on Sun Jan 10 19:29:33 2021

@author: shengrihui
"""
import random
from sortp import *
from prepare import *

    
def disp(p):
    x=''
    for i in p:
        x += i+' '
    return x



#def叫地主（三个玩家的名字）
def jiaodz(p1,p2,p3):   
    '''
    def put判断输入是否正确
    '''
    def  put(t):
        print('\n'*10 if z!=[] else '')
        x=input('玩家{}：\n你的牌是{}\n剩余的牌是：{}\n你是否叫地主？（Y/N）：'.format(t,disp(sort_pai(p[a.index(t)+1])),disp(sort_pai(rest))))
        while 1:
            if not(x=='n' or x=='N' or x=='Y' or x=='y'):
                print('输入有误哦，再来一次吧。（不区分大小写哦）')
                x=input('玩家{}是否叫地主？（Y/N）：'.format(t))
            if x=='Y' or x=='y':
                z.append(t)
                break
            elif x=='N' or x=='n':
                break
    
    '''
    c用来统计全部人都不叫地主的次数，如果有3次，则第三次开始的第一个人就是地主
    '''
    c=0
    a=[p1,p2,p3]
    random.shuffle(a)
    while 1:
        '''p中存放发牌后的一些结果'''
        p=fapai()
        rest,player1,player2,player3=p
        
        '''
        z用来记录选择叫地主的玩家，
        如果三个都选择叫地主，则在问第一个人（a[0]）
        最后,z的最后一个是地主
        '''
        z=[]
        for i in a:
            put(i)
        if len(z) != 0 :
            if len(z) == 3:
                put(a[0])
            '''
            将rest的三张牌给地主
            a中是三个玩家的名字，z的最后一个是地主的名字，
            p中[1:]目前任意对应三个人的牌，现在将rest给到地主
            '''
            p[a.index(z[-1])+1].extend(rest)
            break
        else :
            c += 1
            if c==3:
                p[a.index(a[0])+1].extend(rest)
                break
            else:
                a=a[1:]+a[:1]
    player1=sort_pai(player1)
    player2=sort_pai(player2)
    player3=sort_pai(player3)
    return list(zip(a,[player1,player2,player3]))

if __name__=='__main__':
    t=jiaodz('srh','spyder','python')
    for i in t:
        print(i)
        if len(i[1])==20:
            print('%s是地主' %i[0])
            