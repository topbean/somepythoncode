#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 20:24:43 2019

@author: Gabriel

"""

import pandas as pd
# import openpyxl
# import datetime


score_list = {'2018-09-01': 100, '2018-09-02': 100, '2018-09-03': 70, '2018-09-04': 75, '2018-12-01': 100}
data = pd.DataFrame.from_dict(score_list, orient='index', columns=['score'])



# data = pd.DataFrame.from_dict(score_list, orient='index', columns=['score'])
# data.index.name = 'date'  # 将行索引那一列命名为date
# data.reset_index()  # 重置索引

data = pd.DataFrame(list(score_list.items()), columns=['date', 'score'])



print(data)

data.to_excel('score_test1.xlsx',index=False)