# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 22:22:32 2021

@author: shengrihui
"""

import shutil

shutil.copyfile("a.txt","a_copy.txt")
shutil.copyfile("a.txt","book/a_copy2.txt")

shutil.copytree("book","book_copy")

shutil.copytree("../04文件","book_copy2",ignore=shutil.ignore_patterns("*.py","*.txt"))

import zipfile
import os
'''
shutil.make_archive("zip/book_copy2_zip","zip","book_copy2")

z1=zipfile.ZipFile("zip/a.zip","w")
path=os.getcwd()
for dirpath,dirnames,filenames in os.walk(path):
    if dirpath==os.path.join(path,'zip'):
        continue
    for filename in filenames:
        z1.write(os.path.join(dirpath,filename))
    
z1.close()

z2=zipfile.ZipFile("zip/a.zip",'r')
z2.extractall('zip')
z2.close()

'''


