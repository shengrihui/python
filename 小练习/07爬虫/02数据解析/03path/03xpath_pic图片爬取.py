# -*- coding: utf-8 -*-
"""
Created on Sat Apr 17 10:56:08 2021

@author: shengrihui
"""
# xpath爬取图片

'''
图片box的div
<div class="image-box"><img class="lazy" data-original="//preview.qiantucdn.com/58pic/36/47/58/95t58PICqMT4Pcseeze58PIC7_PIC2018.jpg!kuan320" src="//preview.qiantucdn.com/58pic/36/47/58/95t58PICqMT4Pcseeze58PIC7_PIC2018.jpg!kuan320" alt="金色纹理背景" title="金色纹理背景" style="display: block;"><img class="lazy gs-bg" data-original="//preview.qiantucdn.com/58pic/36/47/58/95t58PICqMT4Pcseeze58PIC7_PIC2018.jpg!kuan320" src="//preview.qiantucdn.com/58pic/36/47/58/95t58PICqMT4Pcseeze58PIC7_PIC2018.jpg!kuan320" alt="金色纹理背景" title="金色纹理背景" style="display: block;"><span class="is-business is-normal"></span><div class="model-box icon-new-box"></div><div class="fav-icon handle-fav" data-id="36475895" data-action="addFav" data-fnum="1"><i class="icon icon-shoucang"><em>收藏</em></i></div><button class="qtw-button qtw-button--jx download-page" data-source="17" data-id="36475895" data-yc="1" data-bg="0"><i class="icon icon-xiazai"></i><span>免费下载</span></button></div>

<div class="qtw-card item" key="1" stats-point="1121" data-w="495" data-h="320" style="width: 388px; height: 251px; display: block;"><a href="//www.58pic.com/newpic/36388737.html" target="_blank" data-id="36388737"><!-- 图片卡片 --><div class="image-box"><img class="lazy" data-original="//preview.qiantucdn.com/58pic/36/38/87/37258PIC997ATrd6jSy28_PIC2018.jpg!kuan320" src="//preview.qiantucdn.com/58pic/36/38/87/37258PIC997ATrd6jSy28_PIC2018.jpg!kuan320" alt="银色灰色背景" title="银色灰色背景" style="display: block;"><img class="lazy gs-bg" data-original="//preview.qiantucdn.com/58pic/36/38/87/37258PIC997ATrd6jSy28_PIC2018.jpg!kuan320" src="//preview.qiantucdn.com/58pic/36/38/87/37258PIC997ATrd6jSy28_PIC2018.jpg!kuan320" alt="银色灰色背景" title="银色灰色背景" style="display: block;"><span class="is-business is-normal"></span><div class="model-box icon-new-box"></div><div class="fav-icon handle-fav" data-id="36388737" data-action="addFav" data-fnum="1"><i class="icon icon-shoucang"><em>收藏</em></i></div><button class="qtw-button qtw-button--jx download-page" data-source="17" data-id="36388737" data-yc="1" data-bg="0"><i class="icon icon-xiazai"></i><span>免费下载</span></button></div><div class="text-box  "><span class="pic-type is-jx">摄影图</span><span class="title">银色灰色背景</span><span class="icon_num"><i class="icon icon-shoucangjiazuopinshu"></i>个</span><div class="more">...</div></div></a></div>

img标签
<img class="lazy" 
data-original="//preview.qiantucdn.com/58pic/36/43/54/33e58PIC56Sfx7B3277Dd_PIC2018.jpg!kuan320" 
src="//preview.qiantucdn.com/58pic/36/43/54/33e58PIC56Sfx7B3277Dd_PIC2018.jpg!kuan320" 
alt="金箔" title="金箔" style="display: block;">


图片地址
https://preview.qiantucdn.com/58pic/36/43/54/33e58PIC56Sfx7B3277Dd_PIC2018.jpg!w1024_new_small
'''

import requests
from lxml import etree
import os

if not os.path.exists('03pic图片爬取'):
    os.makedirs('03pic图片爬取')

url = 'https://www.58pic.com/piccate/53-0-0.html?tid=1101759&utm_source=baidu&utm_medium=cpc&utm_campaign=%C9%E3%D3%B0%CD%BC&utm_content=%C9%E3%D3%B0%CD%BC%BA%CB%D0%C4&utm_term=%CD%BC%C6%AC&sdclkid=ALfG15fsxrDibLepAL26&bd_vid=12670257635697815590'

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'
}

page_text = requests.get(url=url, headers=header).text

tree = etree.HTML(page_text)

div_list = tree.xpath('//div[@class="image-box"]')

for div in div_list[:-1]:
    img_data_original = div.xpath('./img[@class="lazy"]/@data-original')[0]
    img_src = div.xpath('./img[@class="lazy"]/@src')[0]
    # 发现这两个东西是不一样的。
    # print(img_data_original)
    # print(img_src)
    # print(img_data_original==img_src)

    img_name = div.xpath('./img/@title')[0]

    img_url = ''.join(['https:', img_data_original.strip('!kuan320'), '!w1024_new_small'])
    # print(img_url)

    img_data = requests.get(url=img_url, headers=header).content

    img_path = '03pic图片爬取/' + img_name + '.jpg'
    with open(img_path, 'wb') as fp:
        fp.write(img_data)
    print(img_name, '完成')
