# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 21:30:29 2021

@author: shengrihui
"""

import xlrd

#获取excel工作部
data=xlrd.open_workbook("中国省份和城市对照表及城市分级.xlsx")
print(data)

#获取工作表
table=data.sheet_by_index(2)
print(data.sheet_names())


print("sheet3总行数：",table.nrows)
print("sheet3总列数：",table.ncols)


#整row
#for i in range(table.nrows):
    #print(table.row_values(i))


#整col
#for i in range(table.ncols):
    #print(table.col_values(i))


#for i in range(2):
    #for j in range(2):
        #print(table.cell(i,j))

#B3单元格
#cell(row,col)
#cell(3,B)
print(table.cell(2,1).vaule)


