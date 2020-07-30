#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 10:32:21 2019

@author: Gabriel

"""
import datetime
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import pearsonr

# x = [1,2,3]
# y = [2,4,6]

# plt.plot(x,y, color= 'red', linewidth=3, linestyle= '--' )

# plt.show

# 设置中文格式为黑体
plt.rcParams['font.sans-serif'] = ['SimHei']  
plt.rcParams['axes.unicode_minus'] = False  

# 读取数据
data = pd.read_excel('data.xlsx')

#  把日期由string字符串格式转为timestamp时间戳格式，方便坐标轴显示
d = []
for i in range(len(data)):
    d.append(datetime.datetime.strptime(data['date'][i], '%Y-%m-%d'))
data['date'] = d  # 将原来的date那一列数据换成新生成的时间戳格式日期

#  数据可视化并设置双坐标轴
plt.plot(data['date'], data['score'], linestyle='--', label='评分')
plt.xticks(rotation=45)  # 设置x轴刻度显示角度
plt.legend(loc='upper left')  # 分数的图例设置在左上角
plt.twinx()  # 设置双坐标轴
plt.plot(data['date'], data['price'], color='red', label='股价')
plt.xticks(rotation=45)
plt.legend(loc='upper right')
plt.show()


# 相关性分析
corr = pearsonr(data['score'], data['price'])
print('相关系数r值为' + str(corr[0]) + '，显著性水平P值为' + str(corr[1]))