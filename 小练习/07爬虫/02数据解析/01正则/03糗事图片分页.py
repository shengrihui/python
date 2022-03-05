# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 14:55:09 2021

@author: shengrihui
"""

import requests
import re
import os

if not os.path.exists('03qiutulibs'):
    os.makedirs('03qiutulibs')


def pic(url):
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'
    }

    page_text = requests.get(url=url, headers=header).text

    # 获取到了整个页面的数据后，聚焦爬虫
    '''
    <div class="thumb">
    
    <a href="/article/124216845" target="_blank">
    <img src="//pic.qiushibaike.com/system/pictures/12421/124216845/medium/PCE2X1G6RL1I3AWU.jpg" alt="糗事#124216845" class="illustration" width="100%" height="auto">
    </a>
    </div>
    '''
    ex = '<div class="thumb">.*?<img src="(.*?)" alt.*?</div>'
    img_src_list = re.findall(ex, page_text, re.S)
    # print(img_src_list)

    for src in img_src_list:
        # 拼接src
        src = 'https:' + src
        # get请求
        img_data = requests.get(url=src, headers=header).content

        img_name = src.split('/')[-1]
        img_path = '02qiutulibs/' + img_name
        with open(img_path, 'wb') as fp:
            fp.write(img_data)
            print(img_name, '完成！')


for pagenum in range(1, 5):
    url = 'https://www.qiushibaike.com/imgrank/page/{}/'.format(pagenum)
    pic(url)
