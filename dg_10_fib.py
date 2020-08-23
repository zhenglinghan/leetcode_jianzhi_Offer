#!/usr/bin/env python 
# encoding: utf-8 

"""
@version: v1.0
@author: zhenglinghan
@contact: 422807471@qq.com
@software: PyCharm
@file: dg_10_fib.py
@time: 2020/8/22 23:59
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
    # def fib(self, n):
    #     if (n < 2):
    #         return n
    #     return (self.fib(n - 1) + self.fib(n - 2))%1000000007 # 防止越界
    # def fib(self, n):
    #     records = [-1 for i in range(n+1)] # 记录计算的值
    #     if n == 0:return 0
    #     if n == 1:return 1
    #     if records[n] == -1: # 表明这个值没有算过
    #         records[n] = (self.fib(n-1) +self.fib(n-2))%1000000007
    #     return records[n]
    # 动态规划
    def fib(self, n):
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a % 1000000007

if __name__ == "__main__":
    pass 