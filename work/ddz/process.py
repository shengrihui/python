# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 22:44:51 2021

@author: shengrihui
"""


from sortp import*
from err import err
from type import pai_type as ty
from jdz import *


player1_name=input('请输入玩家1的名字：')
player2_name=input('请输入玩家2的名字：')
player3_name=input('请输入玩家3的名字：')
player_name_list=[player1_name,player2_name,player3_name]


#player_name_list=['shengrihui','python','spyder']
t=jiaodz(*player_name_list)
play=[[k,v] for k,v in t]
for i in play:
    if len(i[1])==20 :
        i[0]='地主'+i[0]
        dzn=play.index(i)
    else:
        i[0]='农民'+i[0]
play=play[dzn:]+play[:dzn]

def isv():
    for i in play:
        if len(i[1])==0:
            return True
    else:
        return False


def compare(a,b):
    if b==[] or ty(a)=='王炸':
        return True
    if ty(a)=='炸弹':
        return True
    elif ty(a)==ty(b):
        if sort_v(a[0])>sort_v(b[0]):
             return True
    return False


pas=0
cp_be=[]
lastcon=''
for i in play*1000:
    cou=[[j[0],'还有%d张牌'%(len(j[1]))] for j in play if j[0]!=i[0] ]
    con='{0}{1}现在，{2}{3}，{4}{5}'.format(lastcon,'\n' if lastcon!='' else '',cou[0][0],cou[0][1],cou[1][0],cou[1][1])
    print('\n'*30+'{}：\n{},\n你的牌还有：{}'.format(i[0],con,disp(i[1])))
    
    cp_pai=input('{}请出牌：'.format(i[0]))
    while 1:
        if pas == 2:
            cp_be=[]
        if cp_pai=='pass' or cp_pai=='PASS':
            if cp_be ==[] :
                print('你不能过哦。')
                cp_pai=input('{}请出牌：'.format(i[0]))
                continue 
            if  pas <2:
                pas+=1
                lastcon +='\n{}出牌：过'.format(i[0])
                break
        try:
            cp_pai=cp_pai.upper()
            cptt=['10' for j in range(cp_pai.count('10'))]
            for j in cp_pai:
                try:
                    if j in pai_list :
                        cptt.append(j)
                except:
                    break
            cp_pai=cptt
            cp_pai=sort_pai_c(cp_pai)
        except:
            print('这牌出的不对哦。')
            cp_pai=input('{}请出牌：'.format(i[0]))
        else:
            if compare(cp_pai,cp_be) :
                cp_be=cp_pai
                for j in cp_pai:
                    i[1].remove(j)
                la='{}出出牌：{} {}'.format(i[0],ty(cp_pai),disp(cp_pai))
                lastcon += ('\n'+la if lastcon!='' else la)
                pas=0
                break
            else:
                print('这牌没法打人家哦。')
                cp_pai=input('{}请出牌：'.format(i[0]))
        
    if  isv():
        print('{}胜利！'.format(i[0]))
        break
    
    
