#!/usr/bin/env python 
# encoding: utf-8 

"""
@version: v1.0
@author: zhenglinghan
@contact: 422807471@qq.com
@software: PyCharm
@file: dp_60_twoSum.py
@time: 2020/10/4 0:47
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
    # 二维动态规划
    def twoSum(self, n):
        dp = [[0 for _ in range(6*n+1)] for _ in range(n+1)]# F(n,s) n为塞子个数行 s为点数和（总计n*6种可能）
        # 初始化
        for i in range(1,7):
            dp[1][i] = 1
        # 转移方程：F(n,s) = sum(F(n-1,s-i)) i [1,6]
        for i in range(2,n+1):# n转移
            for j in range(i,i*6+1):# s转移
                for k in range(1,7):
                    dp[i][j] += dp[i-1][j-k]
        # 对最后一行都/6**n即可
        res = []
        for i in range(n,n*6+1):# 所有可能的值！从n到6*n
            res.append(dp[-1][i]/6**n)
        return res

if __name__ == "__main__":
    pass 