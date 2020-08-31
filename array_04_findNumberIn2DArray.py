#!/usr/bin/env python 
# encoding: utf-8 

"""
@version: v1.0
@author: zhenglinghan
@contact: 422807471@qq.com
@software: PyCharm
@file: array_04_findNumberIn2DArray.py
@time: 2020/8/31 23:59
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
    def binary_search(self, matrix, target, start, vertical):
        lo = start
        hi = len(matrix) - 1 if vertical else len(matrix[0]) - 1 # 垂直搜索：hi = 行数 - 1

        while lo <= hi:
            mid = (lo + hi) // 2
            if vertical:  # 垂直搜索
                if matrix[mid][start] < target:
                    lo = mid + 1
                elif matrix[mid][start] > target:
                    hi = mid - 1
                else:
                    return True
            else:   # 水平搜索
                if matrix[start][mid] < target:
                    lo = mid + 1
                elif matrix[start][mid] > target:
                    hi = mid - 1
                else:
                    return True

        return False

    def findNumberIn2DArray(self, matrix, target):
        if not matrix: return False   # 边界条件

        for i in range(min(len(matrix), len(matrix[0]))):
            vertical_found = self.binary_search(matrix, target, i, True) # 垂直方向是否找到
            horizontal_found = self.binary_search(matrix, target, i, False) # 水平是否找到
            if vertical_found or horizontal_found:  # 任一方向找到即可
                return True

        return False


if __name__ == "__main__":
    pass 