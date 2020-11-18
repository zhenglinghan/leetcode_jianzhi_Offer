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
        '''
        该做法精简了DP空间 利用哈希表确定集中分支的状态转移
        :param s:
        :return:
        '''
        dic = {}
        res, tmp = 0, 0
        # tmp 意思是dp[j] 以字符s[j] 为结尾，最长不重复子字符串 的长度
        # 一般dp都更新到最后一位，返回df[-1]
        # 这里通过右边界的形式更新，更新的不是当前全局max，而是右边界max 最后还要取全局max
        # res表示历史最长 通过遍历不断更新保留当前全局max 最后返回
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

    def lengthOfLongestSubstring_self(self, s):
        '''
        自己写个定义dp空间的
        :param s:
        :return:
        '''
        # dp空间需要判断下是否等于0
        if not s:
            return 0
        dic = {}
        dp = [0 for i in range(len(s))]  # dp[j] 表示以 j 为结尾的 最长的不重复的字符串的长度
        for j in range(len(s)):
            i = dic.get(s[j], -1)  # 历史上最近的一次出现s[j]的索引
            dic[s[j]] = j  # 更新索引
            if i == -1:
                # 没出现过
                dp[j] = dp[j - 1] + 1  # 必然更长+1
            elif j - i > dp[j - 1]:
                # 距离上次出现s[j]已经较dp[j-1]更长，所以s[j]不在dp[j-1]中，dp[j-1]可以+1
                dp[j] = dp[j - 1] + 1  # 必然更长+1
            else:
                # s[i]在dp[j-1]中，等于dp[j]的序列是基于dp[j-1]的序列，被s[i]截断，长度等于j-1
                dp[j] = j-i
        # 返回全局最大
        return max(dp)


if __name__ == "__main__":
    strr = "abcabcbb"
    s = Solution()
    ans = s.lengthOfLongestSubstring_self(strr)
    print(ans)
