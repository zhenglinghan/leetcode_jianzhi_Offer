#!/usr/bin/env python 
# encoding: utf-8 

"""
@version: v1.0
@author: zhenglinghan
@contact: 422807471@qq.com
@software: PyCharm
@file: dp_14_cuttingRopeII.py
@time: 2020/8/26 23:39
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
    def cuttingRope(self, n: int) -> int:
        dp = [0 for _ in range(n + 1)]  # dp[0] dp[1]其实没用
        dp[2] = 1  # 初始化
        for i in range(3, n + 1):
            for j in range(i):
                dp[i] = max(dp[i], max((i - j) * j, j * dp[i - j]))
        return dp[n] % 1000000007

    def remainder1(self, x, a, p):
        '''
        循环取余法 保证每轮中间值 rem 都在 int32 取值范围中
        :param x: x^a
        :param a: a次幂 a>0
        :param p: 对p取余
        :return:
        '''
        rem = 1
        for _ in range(a):
            rem = (rem * x) % p
        return rem

    # 求 (x^a) % p —— 快速幂求余
    def remainder2(self, x, a, p):
        rem = 1
        while a > 0:
            if a % 2:
                rem = (rem * x) % p
            x = x ** 2 % p
            a //= 2
        return rem
'''
此题与 面试题14- I. 剪绳子 主体等价，唯一不同在于本题目涉及 “大数越界情况下的求余问题” 。

'''
if __name__ == "__main__":
    pass
