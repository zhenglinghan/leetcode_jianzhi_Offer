#!/usr/bin/env python 
# encoding: utf-8 

"""
@version: v1.0
@author: zhenglinghan
@contact: 422807471@qq.com
@software: PyCharm
@file: dp_19_isMatch.py
@time: 2020/8/28 23:52
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
    def isMatch(self, string, pattern):
        m = len(string)
        n = len(pattern)
        if not m and not n:
            return True
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        string = '#' + string
        pattern = '#' + pattern

        dp[0][0] = True
        for i in range(m + 1):
            for j in range(1, n + 1):
                if i == 0:
                    if j > 1 and pattern[j] == '*':
                        dp[i][j] = dp[i][j - 2]
                elif string[i] == pattern[j] or pattern[j] == '.':
                    dp[i][j] = dp[i - 1][j - 1]
                elif pattern[j] == '*':
                    if string[i] == pattern[j - 1] or pattern[j - 1] == '.':
                        dp[i][j] = dp[i - 1][j] or dp[i][j - 2]
                    else:
                        dp[i][j] = dp[i][j - 2]
        return dp[m][n]

if __name__ == "__main__":
    pass 