# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 22:45:51 2021

@author: shengrihui
"""
from  collections  import defaultdict
from functools import reduce
import time

poem_list=[]

next_word={
    y:defaultdict(set)
    for y in range(5)
    }

line_words=defaultdict(set)


with open('5.txt','r',encoding='utf-8') as f:
    while True:
        s=f.readline().strip()
        if s=='':
            break
        poem_list.append(s)
        
        for x in range(4):
            line_words[x].add(s[x])
            next_word[x][s[x]].add(s[x+1])
        line_words[4].add(s[4])



canbe_line=defaultdict(list)

for poem in poem_list:
    c=[0,0,0,0,0]
    for w in poem:
        for i in range(5):
            if w in line_words[i]:
                c[i]+=1
    for i in range(5):
        if c[i]==5:
            canbe_line[i].append(poem)
 

y_x_w_zlist={
        y:{x:defaultdict(list) for x in range(5)}
        for y in range(5)
        }

z=0
for y in range(5):
    for s in canbe_line[y]:
        for x in range(5):
            y_x_w_zlist[y][x][s[x]].append(z)
        z+=1
    z=0

y_x_z_w={
    y:{x:defaultdict(str) for x in range(5)}
    for y in range(5)
    }
z=0
for y in range(5):
    for s in canbe_line[y]:
        
        for x in range(5):
            y_x_z_w[y][x][z]=s[x]
        z+=1
    z=0

#4444444 
#555555
Forth_Fifth=defaultdict(list)
start=time.time()
y=3
yn=4
n=0
for poem in canbe_line[y]:
    z_sets={
        x:set() for x in range(5)
        }
    for x in range(5):
        w=poem[x]
        next_w_list=next_word[y][w]
        for n_w in next_w_list:
            w_z=y_x_w_zlist[yn][x][n_w]
            z_sets[x].update(w_z)
    z_y_s=reduce(lambda a,b:a&b ,[item for item in z_sets.values()])
    
    if z_y_s==set():
        continue
    for z in z_y_s:
        t=''.join([ y_x_z_w[yn][x][z]  for x in range(5)  ])
        Forth_Fifth[poem].append(t)
    n+=1
    print("\r{}".format(n/len(canbe_line[y])*100),end='')
print()
#print(Forth_Fifth)

stop=time.time()
print(stop-start)


#333333
#444444444
Third_Forth=defaultdict(list)
yn=3
y=2
n=0
start=time.time()
for poem in canbe_line[y]:
    z_sets={
        x:set() for x in range(5)
        }
    for x in range(5):
        w=poem[x]
        next_w_list=next_word[y][w]
        for n_w in next_w_list:
            w_z=y_x_w_zlist[yn][x][n_w]
            z_sets[x].update(w_z)
    z_y_s=reduce(lambda a,b:a&b ,[item for item in z_sets.values()])
    
    if z_y_s==set():
        continue
    for z in z_y_s:
        t=''.join([ y_x_z_w[yn][x][z]  for x in range(5)  ])
        if t in Forth_Fifth:
            for tt in Forth_Fifth[t]:
                app=[t,tt]
                third_Forth[poem].append(app)
    n+=1
    print("\r{}".format(n/len(canbe_line[y])*100),end='')
print() 
#print(Forth_Fifth)

stop=time.time()
print(stop-start)






Second_Third=defaultdict(list)
yn=2
y=1
n=0
start=time.time()
for poem in canbe_line[y]:
    z_sets={
        x:set() for x in range(5)
        }
    for x in range(5):
        w=poem[x]
        next_w_list=next_word[y][w]
        for n_w in next_w_list:
            w_z=y_x_w_zlist[yn][x][n_w]
            z_sets[x].update(w_z)
    z_y_s=reduce(lambda a,b:a&b ,[item for item in z_sets.values()])
    
    if z_y_s==set():
        continue
    for z in z_y_s:
        t=''.join([ y_x_z_w[yn][x][z]  for x in range(5)  ])
        if t in Third_Forth:
            for tt in Third_Forth[t]:
                app=[t,tt]
                Second_Third[poem].append(app)
    n+=1
    print("\r{}".format(n/len(canbe_line[y])*100),end='')
print() 
#print(Forth_Fifth)

stop=time.time()
print(stop-start)






First_Second=defaultdict(list)
yn=1
y=0
n=0
start=time.time()
for poem in canbe_line[y]:
    z_sets={
        x:set() for x in range(5)
        }
    for x in range(5):
        w=poem[x]
        next_w_list=next_word[y][w]
        for n_w in next_w_list:
            w_z=y_x_w_zlist[yn][x][n_w]
            z_sets[x].update(w_z)
    z_y_s=reduce(lambda a,b:a&b ,[item for item in z_sets.values()])
    
    if z_y_s==set():
        continue
    for z in z_y_s:
        t=''.join([ y_x_z_w[yn][x][z]  for x in range(5)  ])
        if t in Third_Forth:
            for tt in Second_Third[t]:
                app=[t,tt]
                First_Second[poem].append(app)
    n+=1
    print("\r{}".format(n/len(canbe_line[y])*100),end='')
print() 
#print(Forth_Fifth)

stop=time.time()
print(stop-start)




print("ok")
        
        