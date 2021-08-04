# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 10:45:44 2021

@author: shengrihui
"""
from prepare import pai_list


def sort_v(t):
    return pai_list.index(t)

def sort_pai(pai,rev=False):
    '''
    对牌进行排序（整理）
    rev正序或倒叙    
    '''
    pai=sorted(pai,key=lambda x:sort_v(x))
    if rev:
        pai=pai[::-1]
    return pai

def count_pai(pai):
    '''
    对玩家所出的牌进行统计整理，方便排序和判断类型
    lp  将原始的牌1.去掉重复 2.从大到小排序（方便后面在出现相同次数的牌中间再排序）
    lc  统计不同地牌在原始牌中出现地次数
    lp_e lc_e s使lp、lc之间建立联系
    lcs  对不同的牌出现的不同次数进行排序
    lpt  再次数排序的基础上，按值排序
    result 输出排序后的牌和次数，一一对应
    '''
    lp=list(set(pai))
    lp.sort(reverse=True,key=lambda x:sort_v(x))
    lc=[pai.count(i) for i in lp]
    lp_e=list(enumerate(lp))
    lc_e=list(enumerate(lc))
    lcs=sorted(lc_e,key=lambda x:x[1],reverse=True)
    lpt=[ j for i in lcs for j in lp_e if i[0]==j[0]  ]
    result_p=[lpt[i][1]for i in range(len(lpt))]
    result_c=[lcs[i][1]for i in range(len(lcs))]
    return result_p,result_c
    
def sort_pai_c(pai):
    p=count_pai(pai)[0]
    c=count_pai(pai)[1]
    lst=[i for i in p for j in range(c[p.index(i)])]
    return lst

            
if __name__=='__main__':
    print(pai_list)
    for i in range(3):
        t=input('出牌:')
        t=t.strip(' ')
        t=t.upper()
        tt=t.split(' ')
        print(sort_pai_c(tt))
    
    

'''
def sort_pai_c(pai):
    lt=zip(count_pai(pai)[0],count_pai(pai)[1])
    lis=sorted(lt,key=lambda x:x[1],reverse=True)
    lst=[]
    t=[lis[0]]
    for i in range(1,len(lis)):
        if lis[i][1]==lis[i-1][1]:
            t.append(lis[i])
        if lis[i][1]!=lis[i-1][1] or i == len(lis)-1:
            lit=[ j[0] for j in t]
            lit=sort_pai(lit,rev=True)
            for j in lit:
                for k in range(lis[i-1][1]):
                    lst.append(j)
            t=[lis[i]]
    return lst
  
'''    
    
    
    
    
    
    
    