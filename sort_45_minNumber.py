#!/usr/bin/env python 
# encoding: utf-8 

"""
@version: v1.0
@author: zhenglinghan
@contact: 422807471@qq.com
@software: PyCharm
@file: sort_45_minNumber.py
@time: 2020/8/11 21:20
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


class Solution(object):
    '''
    快排解法
    字符串排列的大小推导式子：
    if x+y (xy) >y+x (yx)
       z+y (zy) >y+z (yz)
    则 xz < zx
    具有传递性

    所以只要将2数字a,b排序的比较改成 比较a+b 与 b+a
    若a+b>b+a
    等价于认为b<a
    '''

    def minNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        nums = [str(i) for i in nums]
        nums = self.qsort(nums)
        return ''.join(nums)

    def qsort(self, nums):
        if not nums:
            return ['']
        elif len(nums) < 2:
            return [nums[0]]
        else:
            pi = nums[0]
            left = self.qsort([x for x in nums[1:] if x + pi < pi + x])  # 若a+b>b+a 等于 认为 b<a
            right = self.qsort([x for x in nums[1:] if x + pi >= pi + x])
        return left + [pi] + right


if __name__ == "__main__":
    sl = Solution()
    ans = sl.minNumber(['10', '2', '3', '30'])
    print(ans)
