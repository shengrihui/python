# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 18:36:28 2021

@author: shengrihui
"""

import calcu_location
import linear_model
import pandas as pd

#读取文件，类型是dataframe
df=pd.read_excel(u'eqList2020_05_17.xls','Table1')

#经纬度处理
#“北纬N33°15′10.10″ 东经E103°54′52.63″海拔:2813.05米”  九寨沟
e_long=103.52   #经度
e_lat=33.17     #纬度
range_location=calcu_location.calcu_location( e_lat ,e_long ,300)
location_long=range_location['location_y']
location_lat=range_location['location_x']

#根据经纬度范围来筛选数据

range_data=df[
    (df['纬度(°)'] < location_lat.get('max')) &
    (df['纬度(°)'] > location_lat.get('min')) &
    (df['经度(°)'] < location_long.get('max')) &
    (df['经度(°)'] > location_long.get('min')) 
    ]

#将时间转为日期格式数据
range_data['发震时刻']=pd.to_datetime(range_data['发震时刻'])
#将时间作为索引
range_data=range_data.set_index('发震时刻')
#对时间排序
range_data=range_data.sort_index()
#时间范围
start_date='2012-01-01'
end_date='2020-05-01'
range_data=range_data[start_date:end_date]
#震级大于等于6级
range_data_6=range_data[range_data['震级(M)']>=6]


def show_line(tmp_data):
    group1=tmp_data.groupby(['震级(M)'])    
    #nn=list(group1)
    #mm=[ x for x in group1]
    group_size=group1.size()
    p_x=[ [g] for g in group_size.index ]
    linear_model.show_linear_line(p_x,group_size.values)


for index in range_data_6.index:
    temp_data=range_data[start_date:index]
    show_line(temp_data)
    start_date=index
else:
    temp_data=range_data[start_date:end_date]
    show_line(temp_data)
    








