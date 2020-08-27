#!/usr/bin/env python 
# encoding: utf-8 

"""
@version: v1.0
@author: zhenglinghan
@contact: 422807471@qq.com
@software: PyCharm
@file: dp_47_maxValue.py
@time: 2020/8/27 22:53
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

'''
动态规划标准套路
1：找递推公式
2：定义空间去更新

优化细节
1：时间上，边界的循环可以提出来
2：空间上，如果dp空间的递推公式只与自身，以及同维度的入参空间相关，则可以不新建dp空间，就在入参的数据上更新
'''


class Solution:
    def maxValue0(self, grid):
        if not grid:
            return 0
        row_num = len(grid)
        col_num = len(grid[0])
        df = [[0] * col_num for i in range(row_num)]
        for i in range(row_num):
            for j in range(col_num):
                if i == 0 and j == 0:
                    df[i][j] = grid[i][j]
                elif i == 0:
                    df[i][j] = df[i][j - 1] + grid[i][j]
                elif j == 0:
                    df[i][j] = df[i - 1][j] + grid[i][j]
                else:
                    df[i][j] = max(df[i - 1][j], df[i][j - 1]) + grid[i][j]
        return df[row_num - 1][col_num - 1]

    ## 空间优化
    def maxValue1(self, grid):
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == 0 and j == 0: continue
                if i == 0:
                    grid[i][j] += grid[i][j - 1]
                elif j == 0:
                    grid[i][j] += grid[i - 1][j]
                else:
                    grid[i][j] += max(grid[i][j - 1], grid[i - 1][j])
        return grid[-1][-1]

    ## 时间优化
    def maxValue2(self, grid):
        m, n = len(grid), len(grid[0])
        for j in range(1, n):  # 初始化第一行
            grid[0][j] += grid[0][j - 1]
        for i in range(1, m):  # 初始化第一列
            grid[i][0] += grid[i - 1][0]
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] += max(grid[i][j - 1], grid[i - 1][j])
        return grid[-1][-1]
    if __name__ == "__main__":
        pass
