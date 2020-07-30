#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 20:09:25 2019

@author: Gabriel
"""

import pdfplumber
pdf = pdfplumber.open('公司A理财公告.PDF')  # 打开PDF文件
pages = pdf.pages  # 通过pages属性获取所有页的信息，此时pages是一个列表
page = pages[0]  # 获取第一页内容
text = page.extract_text()  # 通过
print(text)  # 打印第一页内容
pdf.close()  # 关闭PDF文件