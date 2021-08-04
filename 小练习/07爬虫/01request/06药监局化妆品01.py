# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 15:38:30 2021

@author: shengrihui
"""

'''
#http://scxk.nmpa.gov.cn:81/xk/
import requests
url='http://scxk.nmpa.gov.cn:81/xk/'
header={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'
    }
response=requests.get(url=url,headers=header)
print(response.text)
print("没有信息")
'''


import requests
import json

header={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'
    }

url='http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList'

all_id_list=[]
for page in range(1,6):
    data1={
           'on': 'true',
           'page': page,
           'pageSize': 15,
           'productName':' ',
            'conditionType': 1,
            'applyname':' '
        }
    id_json=requests.post(url=url,data=data1,headers=header).json()
    id_list=id_json['list']
    
    for i in id_list:
        all_id_list.append(i['ID'])
    

post_url='http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById'
all_details=[]
for i in all_id_list:
    data2={
          'id':i
          }
    detail_json=requests.post(url=post_url,data=data2,headers=header).json()
    all_details.append(detail_json)

fp=open('06.json','w',encoding='utf-8')
json.dump(all_details, fp, ensure_ascii=False)
fp.close()


print('over')