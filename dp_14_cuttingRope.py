#!/usr/bin/env python 
# encoding: utf-8 

"""
@version: v1.0
@author: zhenglinghan
@contact: 422807471@qq.com
@software: PyCharm
@file: dp_14_cuttingRope.py
@time: 2020/8/25 23:09
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
    '''
    数学法
    '''
    def cuttingRope(self, n):
        if n == 2 or n == 3:
            return n - 1
        if n==4:
            return n
        res = 1
        while n > 4:
            # 如果n大于4，我们不停的让他减去3
            n = n - 3
            # 计算每段的乘积
            res = res * 3
        return n * res
    '''
    动态规划法
    '''
    def cuttingRope(self, n):
        dp = [0 for _ in range(n + 1)]  # dp[0] dp[1]其实没用
        dp[2] = 1  # 初始化
        res = -1
        for i in range(3, n + 1):
            for j in range(i):
                dp[i] = max(dp[i], max((i - j) * j, j * dp[i - j]))
        return dp[n]

'''
可以使用动态规划，从已知值 F(2) 逐步迭代到目标值 F(n) 它是一种自底向上的方法。

算法 建立一维动态数组 dp：

边界条件：dp[1] = dp[2] = 1，表示长度为 2 的绳子最大乘积为 1；
状态转移方程：dp[i] = max(dp[i], max((i - j) * j, j * dp[i - j]))，可以这样理解：
max 第一层 原状态之后保持不变 vs 有剪裁的状态 取max
max 第二层 总长i,在j初剪一下，之后保持不变的值 vs 总长i在j处剪一下剪下来的部分还要继续剪 取max

'''
if __name__ == "__main__":
    pass 