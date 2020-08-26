#!/usr/bin/env python 
# encoding: utf-8 

"""
@version: v1.0
@author: zhenglinghan
@contact: 422807471@qq.com
@software: PyCharm
@file: df_42_maxSubArray.py
@time: 2020/8/27 0:15
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
    def maxSubArray_fail(self, nums):
        '''
        暴力法
        :param nums:
        :return:
        '''
        dp = [-100 for _ in range(len(nums))]
        dp[0] = nums[0]  # 初始化
        for i in range(1, len(nums)):
            for j in range(i+1):
                dp[i] = max([dp[i], sum(nums[j:i+1])])
        return max(dp)

    def maxSubArray(self, nums):
        '''
        f(n+1) 只与 f(n) 与 nums[n+1]有关
        只要nums[n+1]>0 则f(n)必然比f(n+1)小
        :param nums:
        :return:
        '''
        for i in range(1, len(nums)):
            nums[i] += max(nums[i - 1], 0)# 就地累加修改！不再占用空间了！
        return max(nums)

'''
动态规划是本题的最优解法，以下按照标准流程解题。
动态规划解析：
状态定义： 设动态规划列表 dp，dp[i] 代表以元素 nums[i] 为结尾的连续子数组最大和。
为何定义最大和 dp[i] 中必须包含元素 nums[i] ：保证 dp[i] 递推到 dp[i+1] 的正确性；如果不包含 nums[i]，递推时则不满足题目的连续子数组要求。
转移方程： 若 dp[i−1]≤0 ，说明 dp[i - 1]对 dp[i] 产生负贡献，即 dp[i-1] + nums[i] 还不如 nums[i] 本身大。
当 dp[i - 1] > 0 时：执行 dp[i] = dp[i-1] + nums[i]；
当 dp[i−1]≤0 时：执行 dp[i] = nums[i]；
初始状态： dp[0] = nums[0]，即以 nums[0]结尾的连续子数组最大和为nums[0]。
返回值： 返回 dp 列表中的最大值，代表全局最大值
'''
if __name__ == "__main__":
    pass 