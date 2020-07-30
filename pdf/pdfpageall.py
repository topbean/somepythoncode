#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 20:12:46 2019

@author: Gabriel
"""

# 2.解析全部PDF页数的文本信息
import pdfplumber
import jieba

pdf = pdfplumber.open('公司A理财公告.PDF')
pages = pdf.pages
text_all = []
for page in pages:  # 遍历pages中每一页的信息
    text = page.extract_text()  # 提取当页的文本内容
    text_all.append(text)  # 通过列表.append()方法汇总每一页内容
text_all = ''.join(text_all)  # 把列表转换成字符串

f = open (r'公司A理财公告.txt','w')
print(text_all,file = f)  # 打印全部文本内容

# print(text_all)  # 打印全部文本内容
pdf.close()


report = open('公司A理财公告.txt', 'r').read()
words = jieba.cut(report)  
report_words = []
for word in words:  # 将大于4个字的词语放入列表
    if len(word) >= 4:
        report_words.append(word)
# print(report_words)


from collections import Counter

result = Counter(report_words).most_common(5)  # 取最多的50组
print(result)