#!/usr/bin/env python 
# encoding: utf-8 

"""
@version: v1.0
@author: zhenglinghan
@contact: 422807471@qq.com
@software: PyCharm
@file: dg_16_myPow.py
@time: 2020/8/23 23:33
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
    # 分指数奇偶 省时间 二分法角度
    def myPow1(self, x, n):
        if n == 0:
            return 1
        if n < 0:
            return (1 / x) * self.myPow(1 / x, -1 * n - 1)
        if n % 2 == 0:
            return self.myPow(x * x, n // 2)
        else:
            return x * self.myPow(x * x, n // 2)

    # 二进制 位运算法！
    def myPow2(self, x, n):
        if x == 0:
            return 0
        res = 1
        if n < 0:
            x, n = 1 / x, -n
        while n:
            if n & 1:
                res *= x
            x *= x
            n >>= 1
        return res


if __name__ == "__main__":
    s = Solution()
    x = 2
    n = 10
    ans = s.myPow2(x, n)
    print(ans)
