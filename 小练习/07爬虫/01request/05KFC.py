# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 21:29:11 2021

@author: shengrihui
"""
'''
import requests
import json

url='http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname'
header={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'
    }
#city=input('input a city name:')
city='北京'
list_data=""
for i in range(1,8):
    data={
          'cname':city,
          'pid':' ',
          'pageIndex': i,
          'pageSize': 10
          }
    response=requests.post(url=url, data=data, headers=header)
    
    
    list_data+=response.text

print(list_data)

f=open('05KFC.json','w',encoding='utf-8') 
json.dump(list_data, f, ensure_ascii=False)
f.close()    


'''
import requests
import json

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'
}

url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'

city = input("xxx:yu")
data = {
    'cname': '',
    'pid': '',
    'keyword': city,
    'pageIndex': '1',
    'pageSize': '10',
}

response = requests.post(url=url, data=data, headers=headers)

list_data = response.text
print(response)
print(list_data)
