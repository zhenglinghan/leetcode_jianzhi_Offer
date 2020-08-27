#!/usr/bin/env python 
# encoding: utf-8 

"""
@version: v1.0
@author: zhenglinghan
@contact: 422807471@qq.com
@software: PyCharm
@file: dp_63_maxProfit.py
@time: 2020/8/27 23:36
"""

import pandas as pd
import numpy as np
import os
import gc
import datetime as dt
import warnings

warnings.filterwarnings("ignore")
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('precision', 5)
pd.set_option('display.float_format', lambda x: '%.5f' % x)
pd.set_option('max_colwidth', 200)
pd.set_option('display.width', 5000)


class Solution:
    def maxProfit(self, prices):
        cost, profit = float("+inf"), 0  # 初始化cost!
        for price in prices:
            cost = min(cost, price)
            profit = max(profit, price - cost)
        return profit


'''
思考方式：一维序列就不要想去做二维的dp空间，买入点相对好确定着去更新，卖出点是要dp更新的
dp[i]=max(dp[i-1],i天卖出的最大利益) dp空间内的值总表示过去到现在的最xxx值
df[i]=max(df[i-1],price[i]-min(price[:i]))

空间优化：一维的dp 如果递推公式只和自己i-1有关，可以用一个值替代dp空间
pf = max(pf,price[i]-min(price[:i]))

时间优化：因为每次都算price[:i],可以用一个动态更新的维护的mincost 来代替每次计算过去所有，只要每次更新用当前值和mincost做更新就可以
pf = max(pf,max(price - cost))
'''
if __name__ == "__main__":
    pass
