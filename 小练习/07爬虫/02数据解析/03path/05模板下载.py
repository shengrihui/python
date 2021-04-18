# -*- coding: utf-8 -*-
"""
Created on Sat Apr 17 14:26:00 2021

@author: shengrihui
"""

import requests
from lxml import etree
import os

if not os.path.exists('05模板下载'):
    os.makedirs('05模板下载')

count=0     #下载数量
success=0   #下载成功数量

def one_page(page_iindex):
    global count,success
    url='https://aspx.sc.chinaz.com/query.aspx?keyword=%E5%85%8D%E8%B4%B9&issale=&classID=864&page={}'.format(page_iindex)

    header={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'
        }
    
    page_text=requests.get(url=url,headers=header).text
    tree=etree.HTML(page_text)
    #print(page_text)
    
    '''
    <div class="box col3 ws_block masonry-brick" style="width: 219px; height: 342px; position: absolute; top: 732px; left: 482px;"> 
		<a target="_blank" href="//sc.chinaz.com/jianli/201019063460.htm">
			<img src="//scpic.chinaz.net/Files/pic/jianli/202010/jianli13812_s.jpg" alt="ui设计简历模板免费下载">
		</a>
		<p><a class="title_wl" target="_blank" href="//sc.chinaz.com/jianli/201019063460.htm">ui设计简历模板免费下载</a>
        </p>
    </div>
    '''
    
    div_list=tree.xpath('//div[@class="box col3 ws_block"]')
    #div每一个模板
    for div in div_list:
        count+=1
        #取模板的url
        a_url='https:'+div.xpath('./a/@href')[0]
        template_name=div.xpath("./p/a/text()")[0]
        try:
            template_page=requests.get(url=a_url,headers=header).text
        except:
            continue
        t_tree=etree.HTML(template_page)
        
        '''
        <div class="clearfix mt20 downlist">
        '''
        
        #下载连接
        a_download_list=t_tree.xpath('//div[@class="clearfix mt20 downlist"]//a/@href')
        
        #如果有下载链接下不来了，换一个，直到下载完成
        a_i=0
        while True:
            try:
                data=requests.get(url=a_download_list[a_i],headers=header).content
                break
            except:
                if a_i<len(a_download_list):
                    a_i+=1
                else:
                    break
        
        rar_path='05模板下载/{}'.format(count)+template_name+'.rar'
        with open(rar_path,'wb') as fp:
            fp.write(data)
        
        success+=1
        print(count,template_name,'下载完成')
                                     
    
if __name__=='__main__':
    for i in range(1,25):
        one_page(i)
    print('成功下载',success)
    
    
    