# -*- coding: utf-8 -*-
"""
Created on Fri May  8 15:27:29 2020

@author: Eternal
"""

# coding=utf-8

import xlrd

def read_xlrd(excelFile):
    data = xlrd.open_workbook(excelFile)
    table = data.sheet_by_index(2)
    #dataFile = []
    dict_data={}
    for rowNum in range(table.nrows):
        # if 去掉表头
        if rowNum > 1:
            #dataFile.append(table.row_values(rowNum))
            #
            list_data=table.row_values(rowNum)
            dict_data[list_data[2]]=list_data[3] if list_data[3]!="" else "暂无数据"

    return dict_data


if __name__ == '__main__':
    excelFile = '中国省份和城市对照表及城市分级.xlsx'
    dict_info=read_xlrd(excelFile=excelFile)
    print("-"*50)
    print("请输入功能编码：0 为退出；1为查询城市信息")    
    print("-"*50)
    
    
    while True:
        # 0：退出  1：进行查询
        input_num=eval(input("请输入功能编码："))
        if input_num==0:
            break
        if input_num==1:
            input_info=input("请输入需要查询的城市名称：")
            if input_info in dict_info:
                print(dict_info[input_info])
            else:
                print("请输入有效的城市名称，例如：'上海市'")
            
        
    
    
    
    
    
    
    
    
    