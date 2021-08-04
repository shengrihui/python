# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 13:57:36 2021

@author: shengrihui
"""


from  collections  import defaultdict
import time

#全部诗的list
poem_list=[]

#能成为第某行的句子
canbe_nline=[
    set(),
    set(),
    set(),
    set(),
    set(),
    ]

#第1、2、3、4、5行的索引（第一个字）
#第n个字典存的是能放在第n行字
#也就是这句诗的第n个字作为键，诗做值
#因为这句诗能竖着放，那这些字就能放在对应的那一行
#用字典为了查找更快。
one_word=[
       defaultdict(list),
       defaultdict(list),
       defaultdict(list),
       defaultdict(list),
       defaultdict(list),
       ]

#前2、3、4个字的索引
#和上一个类似。
n_word=[
       defaultdict(list),
       defaultdict(list),
       defaultdict(list),
       ]

with open('5.txt','r',encoding='utf-8') as f:
    while True:
        s=f.readline().strip()
        if s=='':
            break
        poem_list.append(s)
        for i in range(5):
            one_word[i][s[i]].append(s)
        for i in range(3):
            n_word[i][s[0:i+2]].append(s)

#返回某一句诗可能成为哪些行
def n_line(s):
    result=[]
    c=[0,0,0,0,0]
    for i in s:
        for w in range(5):
            if i in one_word[w]:
                c[w]+=1
    #如果这句诗的5个字都能成为其他诗的第n个字，
    #那这句诗就有可能成为第n行
    for i in range(5):
        if c[i]==5:
            result.append(i)
    return result

#填充canbe_列表
for s in poem_list:
   for i in n_line(s):
       canbe_nline[i].add(s)

#print([ len(i) for i in canbe_nline])

#n索引，第几个数
def get_n_word(n,lis):
    t=''
    s=''.join([ se[n] for se in lis ])
    return s

print("ooo")
poem_set=set(poem_list)
aa=[]
bb=[]
start=time.time()
for row0 in poem_list[:1000]:
    #row0，第一行
    col0_row0=row0[0]   #取第一个字
    #print('col0_row0',col0_row0)
    
    for col0 in one_word[0][col0_row0]:
        #rint('col0',col0)
        col0_row1=col0[1]
        col0_row2=col0[2]
        col0_row3=col0[3]
        col0_row4=col0[4]
        #print('col0_row1',col0_row1)
        #由第一列第二个字取出可能的第二行
        for row1 in one_word[0][col0_row1]:
            for row2 in one_word[0][col0_row2]:
                for row3 in one_word[0][col0_row3]:
                    for row4 in one_word[0][col0_row4]:
                        #c计算第二行剩下的4个字和第一型的字组合能不能成为一首诗的前二各自
                        c=0
                        for w in range(1,5):
                            
                            t=''.join([row0[w],row1[w],row2[w],row3[w],row4[w]])
                            if t in poem_set:
                                c+=1
                            else:
                                break
                        else:
                            if c==4:
                                bb.append('{}\t{}'.format(row0,row1))
                                #print('row1',row1)
                    
        
    print('\r{}'.format(poem_list.index(row0)/len(poem_list)*100),end='')
print()
#print(bb)
print(len(bb))
stop=time.time()
print(stop-start)











'''
canbe_nline_list=[ list(i) for i in canbe_nline ]
bb=[]
start=time.time()
for row0 in canbe_nline_list[0][:1000]:
    for row1 in canbe_nline_list[1]:
        c1=0
        for w in range(1,5):
                
            t=''.join([row0[w],row1[w]])
            if t in n_word[0]:
                c1+=1
            else:
                break
        else:
            if c1==4:
                bb.append('{}\t{}'.format(row0,row1))
                #print('row1',row1)
    print('\r{}'.format(canbe_nline_list[0].index(row0)/1000*100),end='')
print()
#print(bb)
print(len(bb))
stop=time.time()
print(stop-start)
'''












'''
#print(poem_list)
print(len(poem_list))
print([ len(i) for i in n_word])

print([len(i) for i in canbe_nline])
print([len(i) for i in one_word])
tt=one_word[0]
print( sum( [len(i) for i in tt.values()])/len(tt))

print("read over\n")
c=0
two=[]
for i in canbe_nline[0]:
    t=[i]
    for j in canbe_nline[1]:
        t.append(j)
        cc=0
        for k in range(5):
            if get_n_word(k, t) in n_word[0]:
                cc+=1
            else:
                break
        else:
            if c==5:
                two.append(t)
        t=[i]
        c+=1
        print(c)
        #print("\r{}".format(round(100*c/(len(canbe_nline[0])*len(canbe_nline[1])),2)),end='')
print(two)

'''




