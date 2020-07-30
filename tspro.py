#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 08:43:45 2019

@author: Gabriel
"""

import tushare as ts

# token = '068f53b27b560480033ab0dbfd549adfa5c8eb9c18568e119d48bca6'
# ts.set_token(token)
# pro=ts.pro_api()


pro = ts.pro_api('068f53b27b560480033ab0dbfd549adfa5c8eb9c18568e119d48bca6')

print(ts.__version__)


# data = pro.income(ts_code='000100.SZ', start_date='20190101', end_date='20191126')


data = pro.cashflow(ts_code='000100.SZ', start_date='20190101', end_date='20191126')


print(data)