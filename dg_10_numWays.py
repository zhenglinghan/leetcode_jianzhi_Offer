#!/usr/bin/env python 
# encoding: utf-8 

"""
@version: v1.0
@author: zhenglinghan
@contact: 422807471@qq.com
@software: PyCharm
@file: dg_10_numWays.py
@time: 2020/8/23 23:16
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
    # 递归
    # 只要最后一步从n-2跳2到n，那之前所有的方案都会和最后一步从n-1跳1到n不同
    # f(n) = f(n-1)+f(n-2)
    # def numWays(self, n):
    #     if n==0:
    #         return 1
    #     if n==1:
    #         return 1
    #     if n==2:
    #         return 2
    #     records = [-1 for i in range(n+1)]
    #     if records[n] == -1: # 表明这个值没有算过
    #         records[n] = (self.numWays(n-1) +self.numWays(n-2))%1000000007
    #     return records[n]
    # 动态规划
    def numWays(self, n):
        a, b = 1, 1
        for _ in range(n):
            a, b = b, a + b
        return a % 1000000007


if __name__ == "__main__":
    pass
