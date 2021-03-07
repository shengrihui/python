# -*- coding: utf-8 -*-
"""
Created on Fri May  8 15:15:40 2020

@author: Eternal
"""
# coding=utf-8

import xlrd

def read_xlrd(excelFile):
    data = xlrd.open_workbook(excelFile)
    table = data.sheet_by_index(2)

    for rowNum in range(table.nrows):
        rowVale = table.row_values(rowNum)
        for colNum in range(table.ncols):
            if rowNum > 1 and colNum == 0:
                print((rowVale[0]))
            else:
                print(rowVale[colNum])
        print("---------------")

    # if判断是将 id 进行格式化
    # print("未格式化Id的数据：")
    # print(table.cell(1, 0))
    # 结果：number:1001.0


if __name__ == '__main__':
    excelFile = '中国省份和城市对照表及城市分级.xlsx'
    read_xlrd(excelFile=excelFile)
    
    
    
    
