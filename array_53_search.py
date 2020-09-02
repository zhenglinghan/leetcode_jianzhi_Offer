#!/usr/bin/env python 
# encoding: utf-8 

"""
@version: v1.0
@author: zhenglinghan
@contact: 422807471@qq.com
@software: PyCharm
@file: array_53_search.py
@time: 2020/9/3 0:00
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
    # 一次二分+向前遍历
    def search1(self, nums, target: int):
        # 特例
        if not nums:
            return 0
        # 搜索右边界 right
        i, j = 0, len(nums) - 1
        while i <= j:
            m = (i + j) // 2
            if nums[m] <= target:
                i = m + 1
            else:
                j = m - 1
        right = i
        # 若数组中无 target ，则提前返回
        if j >= 0 and nums[j] != target:
            return 0
        # 搜索左边界 left
        # 确定下右边界是第一个数时：
        if right == 0 and nums[j] != target:
            return 0
        if right == 0 and nums[j] == target:
            return 1
        # 左边界的遍历起点，一个个向左遍历找到left
        j = i - 1
        while j >= 0:
            if nums[j] != target:
                break
            else:
                j -= 1
        left = j
        return right - left - 1
    # 二次二分！
    def search2(self, nums: [int], target: int) -> int:
        # 搜索右边界 right
        i, j = 0, len(nums) - 1
        while i <= j:
            m = (i + j) // 2
            if nums[m] <= target:
                i = m + 1
            else:
                j = m - 1
        right = i
        # 若数组中无 target ，则提前返回
        if j >= 0 and nums[j] != target: return 0
        # 搜索左边界 left
        i = 0
        while i <= j:
            m = (i + j) // 2
            if nums[m] < target:
                i = m + 1
            else:
                j = m - 1
        left = j
        return right - left - 1


if __name__ == "__main__":
    s = Solution()
    nums = [2, 2]
    target = 2
    ans = s.search1(nums, target)
    print(ans)
