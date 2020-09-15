#!/usr/bin/env python 
# encoding: utf-8 

"""
@version: v1.0
@author: zhenglinghan
@contact: 422807471@qq.com
@software: PyCharm
@file: Math_43_countDigitOne.py
@time: 2020/9/16 0:09
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
    def countDigitOne(self, n):
        digit, res = 1, 0# 位，结果
        high, cur, low = n // 10, n % 10, 0 # 高位， 当前位 ， 低位可以组成n high*10*10^0+cur*10^0+low*10^0
        while high != 0 or cur != 0:
            if cur == 0:
                res += high * digit
            elif cur == 1:
                res += high * digit + low + 1
            else:
                res += (high + 1) * digit
            low += cur * digit # 将 cur 加入 low ，组成下轮 low
            cur = high % 10 # 下轮 cur 是本轮 high 的最低位
            high //= 10 # 将本轮 high 最低位删除，得到下轮 high
            digit *= 10 # 位因子每轮 × 10
        return res


if __name__ == "__main__":
    '''
    总体规律
    now = 1
    for i in [10,100,1000,10000,100000]:   
        dig = np.log10(i)
        if i>10:
            now = now*10+10**(dig-1)
        print(i,now)
    要判断位数是否等于1
    '''