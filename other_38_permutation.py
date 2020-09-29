#!/usr/bin/env python 
# encoding: utf-8 

"""
@version: v1.0
@author: zhenglinghan
@contact: 422807471@qq.com
@software: PyCharm
@file: other_38_permutation.py
@time: 2020/9/29 17:47
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


class Solution1:
    def permutation(self, s):
        c, res = list(s), []

        def dfs(x):
            if x == len(c) - 1:
                res.append(''.join(c))  # 添加排列方案
                return
            dic = set()
            for i in range(x, len(c)):
                if c[i] in dic:
                    continue  # 重复，因此剪枝
                dic.add(c[i])
                c[i], c[x] = c[x], c[i]  # 交换，将 c[i] 固定在第 x 位
                dfs(x + 1)  # 开启固定第 x + 1 位字符
                c[i], c[x] = c[x], c[i]  # 恢复交换

        dfs(0)
        return res


class Solution2:
    def permutation(self, s):
        self.res = []
        n = len(s)

        def backtrack(s, path):
            if not s:
                self.res.append(path)
            seen = set()
            for i in range(len(s)):
                if s[i] in seen: continue
                seen.add(s[i])
                backtrack(s[:i] + s[i + 1:], path + s[i])

        backtrack(s, "")
        return self.res


if __name__ == "__main__":
    s = 'abcde'
    S1 = Solution1()
    ans1 = S1.permutation(s)
    S2 = Solution2()
    ans2 = S2.permutation(s)
    print(ans1)
    print(ans2)