#!/usr/bin/env python 
# encoding: utf-8 

"""
@version: v1.0
@author: zhenglinghan
@contact: 422807471@qq.com
@software: PyCharm
@file: dp_19_isMatch.py
@time: 2020/8/28 23:52
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
    def isMatch(self, string: str, pattern: str) -> bool:
        '''
        因为又要比前一位匹配又要比同一位匹配，所以需要m+1,n+1
        第一位用辅助位，对齐两个匹配的状态，落在同一位写两种条件确定true or false
        状态改变是true->false的部分
        '''
        m = len(string)
        n = len(pattern)
        if not m and not n:
            return True
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        string = '#' + string
        pattern = '#' + pattern
        '''
        第0位是True 两边全空 
        '''
        dp[0][0] = True

        for i in range(m + 1):  # 待匹配字符串
            for j in range(1, n + 1):  # 模式串
                if i == 0:
                    if j > 1 and pattern[j] == '*':
                        # j=2时 若p[j]=='*' 可以用 x* 去和空字符串匹配 * 消去 x
                        #  状态转移自j-2 因为最后两个可以用*消去 *只影响到最近2位
                        dp[i][j] = dp[i][j - 2]
                    # else 都是false
                    # df[0][1] 是false 因为p的第一个字符（哪怕是. *）都不能和空字符串做匹配
                elif string[i] == pattern[j] or pattern[j] == '.':
                    # 全等不会带来状态改变 或者 j位是. 也等于全等
                    # 直接都去掉一位进行比较
                    dp[i][j] = dp[i - 1][j - 1]
                elif pattern[j] == '*':
                    # 看p 的j位有两种情况
                    # 1）如果p[j]== * ,可以接受p[j-1]!=s[i],或者p[j-1] = '
                    #    这种情况等于新增的j-1 ->j 的值取决于dp[i][j-2] 是否能匹配
                    #    或者取决于dp[i-1][j]
                    # 2）不相等！直接dp[i][j] = dp[i][j-2] *的影响只有两位，其他不改变
                    if string[i] == pattern[j - 1] or pattern[j - 1] == '.':
                        dp[i][j] = dp[i - 1][j] or dp[i][j - 2]
                    else:
                        dp[i][j] = dp[i][j - 2]
        return dp[m][n]

if __name__ == "__main__":
    a=''
    b='*'
    s = Solution()
    ans = s.isMatch(a,b)
    print(ans)