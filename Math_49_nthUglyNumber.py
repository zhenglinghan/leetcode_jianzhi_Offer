#!/usr/bin/env python 
# encoding: utf-8 

"""
@version: v1.0
@author: zhenglinghan
@contact: 422807471@qq.com
@software: PyCharm
@file: Math_49_nthUglyNumber.py
@time: 2020/9/13 23:54
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
    充分利用性质：丑数 = 某个较小丑数（索引x）* 某个因子
    构建动态规划 不是从dp[i]->dp[i+1]
    而是遍历，通过查找符合条件的a,b,c 生成dp空间
    最后返回dp[-1]
    '''
    def nthUglyNumber(self, n):
        dp, a, b, c = [1] * n, 0, 0, 0# a,b,c 是某较小丑数的索引
        # 初始化a,b,c
        # xa为首个乘以2后大于xn的丑数
        # xb为首个乘以3后大于xn的丑数
        # xc为首个乘以5后大于xn的丑数
        '''
        若索引 a,b,c 满足以上条件，则可使用递推公式计算下个丑数 xn+1，其为三种情况中的最小值，即：
        xn+1 = min(xa * 2, xb * 3, xc * 5)
        '''
        for i in range(1, n):
            n2, n3, n5 = dp[a] * 2, dp[b] * 3, dp[c] * 5 # 较小丑数* 某个因子
            dp[i] = min(n2, n3, n5)# 显然下一个丑数必然是上述最小值
            # 如何更新a,b,c 命中一次上述条件，取到最小，则下面必然取到更大的 较小丑数……
            if dp[i] == n2:
                a += 1
            if dp[i] == n3:
                b += 1
            if dp[i] == n5:
                c += 1
        return dp[-1]


if __name__ == "__main__":
    pass
