#!/usr/bin/env python 
# encoding: utf-8 

"""
@version: v1.0
@author: zhenglinghan
@contact: 422807471@qq.com
@software: PyCharm
@file: 48_hash_lengthOfLongestSubstrin.py
@time: 2020/9/4 23:59
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
    def lengthOfLongestSubstring(self, s):
        dic = {}
        res, tmp = 0, 0
        # tmp 意思是dp[j] 以字符s[j] 为结尾，最长不重复子字符串 的长度
        # 一般dp都更新到最后一位，返回df[-1]
        # 这里通过右边界的形式更新，更新的不是当前全局max，而是右边界max 最后还要取全局max
        for j in range(len(s)):
            i = dic.get(s[j], -1)  # 获取索引 i# get不到返回-1
            dic[s[j]] = j  # 更新哈希表 把s[j] 左边最近的相同字符 s[i]更新进去
            # 新的字符出现分支+s[i]~s[j] 中间是dp[j-1]的序列，所以dp[j-1]里没有s[j]，+1
            if tmp < j - i:
                tmp = tmp + 1
            else:
                # s[i] 落在dp[j-1]的序列中，则dp[j] 应该等于s[i]的索引~j
                tmp = j - i  # dp[j - 1] -> dp[j]
            # 这个很精髓！
            res = max(res, tmp)  # max(dp[j - 1], dp[j])
        return res


if __name__ == "__main__":
    pass
