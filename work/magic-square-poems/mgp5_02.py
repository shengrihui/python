# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 09:57:06 2021

@author: shengrihui
"""

from  collections  import defaultdict
from functools import reduce
import time
#大矩阵，
x_y_z_w={
       x:{y:defaultdict(str) for y in range(5)}
       for x in range(5)
       }

#全诗列表
poem_list=[]

#第i行的某个字，对应能接在它下面的字的列表
next_word={
    y:defaultdict(list)
    for y in range(5)
    }

z=0
with open('5.txt','r',encoding='utf-8') as f:
    while True:
        s=f.readline().strip()
        if s=='':
            break
        poem_list.append(s)
        for y in range(5):
            for x in range(5):
                x_y_z_w[x][y][z]=s[x]
        z+=1
        for y in range(4):
            next_word[y][s[y]].append(s[y+1])


#不同的字对应的z坐标
x_y_w_zlist={
    x:defaultdict(list)  
    for x in range(5)
    }
for x in range(5):
    for z,w in x_y_z_w[x][y].items():
        x_y_w_zlist[x][w].append(z)


#s传入一句诗，在第y行，res存现在已经组成了的结果
def Search(s,y,res):
    #z坐标的集合，第y行第x个字
    z_sets={
        y:{x:set() for x in range(5)}
        for y in range(5)
        }
    
    #x循环遍历s（用x坐标有用），
    #并将每一个w能对应下一个字组成next_w_list。
    for x in range(5):
        w=s[x]
        next_w_list=next_word[y][w]
        #n_w循环遍历可能下一个字，
        #并将它的zu欧标（列表）返回，
        #因为是列表，所以加到z_sets用update。
        for n_w in next_w_list:
            w_z=x_y_w_zlist[x][n_w]
            z_sets[y][x].update(w_z)
    #对5个x下的z坐标集合取交集，
    #如果空寂则return
    z_y_s=reduce(lambda a,b:a&b ,[item for item in z_sets[y].values()])
    
    if z_y_s==set():
        return None
    for z in z_y_s:
        t=''.join([  x_y_z_w[x][y][z] for x in range(5)  ])
        print(y,t)
        if y==4:
               return t
        else:
            r=Search(t, y+1, res)
            if r!=None:
                return res.append(r)

start=time.time()
z=0
for s in poem_list[13665:13669] :
    res=[]
    print(poem_list.index(s))
    print(Search(s, 0, res))

    #print(z_y_s)
    
    z+=1
    #print("\r{}".format(100*z/len(poem_list)),end='')
    print("\r{}".format(100*z/100),end='')
    

stop=time.time()
print()
print(stop-start)
print("00")

