#!/usr/bin/env python 
# encoding: utf-8 

"""
@version: v1.0
@author: zhenglinghan
@contact: 422807471@qq.com
@software: PyCharm
@file: array_11_minArray.py
@time: 2020/9/22 0:12
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
    def minArray(self, numbers):
        # 二分法
        i, j = 0, len(numbers) - 1
        while i < j:
            m = (i + j) // 2
            if numbers[m] > numbers[j]:
                i = m + 1
            elif numbers[m] < numbers[j]:
                j = m
            else:
                j -= 1
        return numbers[i]

    def minArray2(self, numbers):
        # 线性查找 时间上不理想 当有线性关系时尽量二分法，利用部分必然成立的大小关系，缩减查找量
        if numbers:
            if len(numbers) >= 2:
                i = 0
                while i < len(numbers) - 1 and numbers[i] <= numbers[i + 1]:
                    i += 1
                if i < len(numbers) - 1:
                    return numbers[i + 1]
                else:
                    return numbers[0]

            else:
                return numbers[0]
        else:
            return []


if __name__ == "__main__":
    pass
