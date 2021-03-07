# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 22:03:16 2021

@author: shengrihui
"""

import xlrd

data=xlrd.open_workbook("中国省份和城市对照表及城市分级.xlsx")
table=data.sheet_by_index((2))

def print_province():
    province_list=list(set(table.col_values(1)))
    province_list.remove("")
    print(province_list)


p_c={}
for c in range(2,table.nrows):
    tmp=p_c.get(table.cell(c,1).value,[])
    tmp.append(table.cell(c,2).value)
    p_c[table.cell(c,1).value]=tmp
    #print(p_c)
    
def print_province_citys():
    for p in p_c:
        print(p,":")
        for c in p_c[p]:
            print(c)
        print('-'*20)

def print_province_count():
    p_c_li=[(p,len(c)) for p,c in p_c.items()]
    p_c_li=sorted(p_c_li,key=lambda x: -x[1])
    for i in p_c_li:
        print("{}:{}".format(i[0],i[1]))
    
def print_city_level():
    c_l={}
    for c in range(2,table.nrows):
        if table.cell(c,3).value=='':
            continue
        tmp=c_l.get(table.cell(c,3).value,[])
        tmp.append(table.cell(c,2).value)
        c_l[table.cell(c,3).value]=tmp
    
    for i in c_l:
        print("{}有{}个：".format(i,len(c_l[i])))
        for j in c_l[i]:
            print(j,end=',')
        print()
        print('-'*20)
            
        







#print_province()
#print_province_citys()
#print_province_count()
print_city_level()



