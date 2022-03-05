# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 13:51:41 2021

@author: shengrihui
"""

import requests

url = 'https://pic.qiushibaike.com/system/pictures/12422/124222140/medium/EBZBSXLW6IK0WHN0.jpg'

img_data = requests.get(url=url).content

with open("01.糗图.jpg", "wb") as f:
    f.write(img_data)

print("ok")
