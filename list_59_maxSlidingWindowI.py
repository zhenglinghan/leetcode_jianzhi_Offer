#!/usr/bin/env python 
# encoding: utf-8 

"""
@version: v1.0
@author: zhenglinghan
@contact: 422807471@qq.com
@software: PyCharm
@file: list_59_maxSlidingWindowI.py
@time: 2020/8/24 23:54
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
    先进先出队列 处理好起始，终止
    '''
    def maxSlidingWindow(self, nums, k):
        if not nums:
            return []
        res = [max(nums[:k])]
        while len(nums) > k:
            nums.pop(0)
            res.append(max(nums[:k]))
        return res


if __name__ == "__main__":
    s = Solution()
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    ans = s.maxSlidingWindow(nums, k)
    print(ans)
