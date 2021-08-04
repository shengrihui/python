# -*- coding: utf-8 -*-
"""
Created on Fri May  8 12:33:34 2020

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
            row_list=table.row_values(rowNum)
            #dataFile.append(row_list)
            dict_data[row_list[2]]=row_list[3] if not row_list[3]=="" else "暂无信息"

    return dict_data


if __name__ == '__main__':
    excelFile = '中国省份和城市对照表及城市分级.xlsx'
    a=read_xlrd(excelFile=excelFile)
    #print(a)
    print("-"*30)
    print("输入0：退出查询")
    print("输入1：进行城市信息查询")
    print("-"*30)  
    
    while True:
        #'\033[41m这是背景色1'
        input_num=""
        input_info=""
        try:
            input_num=eval(input("\033[31m请输入功能编号："))
        except:
            input_num=1
        if input_num==0:
            break
        elif input_num==1:
            if input_info=="":
                input_info=input("\033[35m请输入想要查询的城市名称：")            
            if str(input_info) in a:
                print('\033[34m'+a.get(input_info))
            else:
                print("输入城市名称错误！请输入有效的城市名称，例如'上海'")
        else:
            print("请输入有效的功能编号！")
    