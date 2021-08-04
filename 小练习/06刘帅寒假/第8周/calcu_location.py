# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 16:20:43 2021

@author: shengrihui
"""

import math
#计算x千米范围内的最大最小经纬度
'''
location_x,     纬度
location_y,     经度
r=1             范围
'''

def calcu_location(location_x, location_y,r=1):
    lat_range = 180 / math.pi *r / 6372.797     #里面的1代表搜索1km范围之间的
    long_r = lat_range / math.cos( location_x * math.pi / 180 )
    max_lat = location_x + lat_range  #最大纬度
    min_lat = location_x - lat_range  #最小纬度
    max_long = location_y + long_r  #最大经度
    min_long = location_y - long_r  #最小经度
    
    range_xy = {}
    #纬度
    range_xy['location_x'] = {'min':round(min_lat,2), 'max':round(max_lat,2)}
    #经度
    range_xy['location_y'] = {'min':round(min_long,2), 'max':round(max_long,2)}
    return range_xy

if __name__=='__main__':
    x=calcu_location(28.1, 121.14)
    print(x)
    
    