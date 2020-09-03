#!/usr/bin/env python 
# encoding: utf-8 

"""
@version: v1.0
@author: zhenglinghan
@contact: 422807471@qq.com
@software: PyCharm
@file: array_53_missingNumber.py
@time: 2020/9/3 23:18
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
    二分法找索引

    i~j 为空时跳出 i=j时还可以做一轮！ 最后返回i!
    '''

    def missingNumber(self, nums):
        i = 0
        j = len(nums) - 1
        while i <= j:
            m = (i + j) // 2
            if nums[m] == m:
                # 要找的点在右边
                i = m + 1
            if nums[m] != m:
                # 要找的点在左边已经出现
                j = m - 1
        return i


if __name__ == "__main__":
    nums = [0,1,2,3,4,5,6,7,9]
    s = Solution()
    ans = s.missingNumber(nums)
    print(ans)
