# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 09:14:12 2021

@author: shengrihui
"""

import xlrd

def read_xlrd(excelfile):
    data=xlrd.open_workbook(excelfile)
    table=data.sheet_by_index(2)
    
    dict_data={}
    for i in range(2,table.nrows):
        tmp=table.row_values(i)
        dict_data[tmp[2]]=tmp[3] if tmp[3]!='' else "暂无信息"
    
    return dict_data
    
    
if __name__=='__main__':
    excelFile = '中国省份和城市对照表及城市分级.xlsx'
    a=read_xlrd(excelfile=excelFile)
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
            print("请输入有效的功能编号！")
        else:
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
    
    
    
    
    