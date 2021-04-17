# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 15:42:31 2021

@author: shengrihui
"""

from bs4 import BeautifulSoup

fp=open('test.html','r',encoding='utf-8')
soup=BeautifulSoup(fp,'lxml')
fp.close()

#print(soup)

'''
soup.tagName返回第一个该标签的内容
print(soup.a)
print(soup.p)
print(soup.h1)
print(soup.ul)
'''
'''
soup.find('tagName') 相当于soup.tagName
print(soup.find('a'))
print(soup.find('h2'))
'''
'''
find属性定位
#print(soup.find('a',name="WelcomeDialog"))
'''
'''
print(soup.find_all('h2'))
'''
'''
select方法 选择器
#print(soup.select('h3'))
print(soup.select('li > a'))
print(soup.select('ul a')[0])
'''
'''
获取标签之间的文本
print(soup.ul.text)
print('--------------------------')
print(soup.ul.string)
print('--------------------------')
print(soup.ul.get_text())
'''

'''
获取标签的属性值
print(soup.a['name'])
print(soup.select('li>a')[0]['href'])
'''