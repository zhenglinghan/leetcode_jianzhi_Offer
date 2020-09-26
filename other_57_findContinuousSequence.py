#!/usr/bin/env python 
# encoding: utf-8 

"""
@version: v1.0
@author: zhenglinghan
@contact: 422807471@qq.com
@software: PyCharm
@file: other_57_findcontinuousSequence.py
@time: 2020/9/26 23:59
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
    数据计算滑窗法
    计算求和 一个窗只能左边界右移+右边界右移
    只要和超过target 必然需要左边界右移
    和不足target 必然需要右边界右移
    直到左边界> target//2
    '''
    def findContinuousSequence(self, target):
        i = 1 # 滑动窗口的左边界
        j = 1 # 滑动窗口的右边界
        sumi = 0 # 滑动窗口中数字的和
        res = []

        while i <= target // 2:
            if sumi < target:
                # 右边界向右移动
                sumi += j
                j += 1
                if j==target//2+3:
                    break
            elif sumi > target:
                # 左边界向右移动
                sumi -= i
                i += 1
            else:
                # 记录结果
                arr = list(range(i, j))
                res.append(arr)
                # 左边界向右移动
                sumi -= i
                i += 1

        return res


if __name__ == "__main__":
    pass 