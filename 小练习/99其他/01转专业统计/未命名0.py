# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 10:47:35 2021

@author: shengrihui
"""

import xlrd


exfile=xlrd.open_workbook("2020-2021学年秋季学期转专业拟录取名单.xlsx")
table=exfile.sheet_by_index(0)

in_school={}
in_pro={}
out_school={}
out_in={}   #学院流向
in_otherschool={}   #外院转入

for i in range(1,table.nrows):
    r=table.row_values(i)
    if r[6]=='通过':
        in_school[r[3]]=in_school.get(r[3],0)+1
        in_pro[r[4]]=in_pro.get(r[4],0)+1
        out_school[r[5]]=out_school.get(r[5],0)+1
        t="{}-{}".format(r[5],r[3])
        out_in[t]=out_in.get(t,0)+1
        if r[3]!=r[5]:
            in_otherschool[r[3]]=in_otherschool.get(r[3],0)+1
        
        
def pr(d,s):
    re=sorted(d.items(),key=lambda x:-x[1])
    print(s)
    for i ,j in re:
        print(i,j)
    print()

pr(in_school,'转入学院')
pr(in_pro,'转入专业')
pr(out_school,'转出学院')
pr(out_in,'学院流向')
pr(in_otherschool,'转入学院（外院转入）')
print('外院转入的一共有：',sum(in_otherschool.values()))