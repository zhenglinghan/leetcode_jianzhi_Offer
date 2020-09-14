#!/usr/bin/env python 
# encoding: utf-8 

"""
@version: v1.0
@author: zhenglinghan
@contact: 422807471@qq.com
@software: PyCharm
@file: Math_44_findNthDigit.py
@time: 2020/9/15 0:28
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
    整数定位
    1）进制位数，进制位数下的数个数，该进制位数下的数长度 3者递推公式
    2）搜寻方式
    3）除法确定该进制位数下第几个数
    4）取余确定数字内的位数
    '''
    def findNthDigit(self, n: int) -> int:
        # 目标数的10进制位数，该进制下一共多少个数字（用于确定该进制位数下第几个数），该进制下一共多少个位数
        digit, start, count = 1, 1, 9# 起始
        while n > count: # 1.
            n -= count
            start *= 10# 递推公式start = start*10
            digit += 1# # digit = digit+1
            count = 9 * start * digit# count = 9*digit*start
        # 找到对应的digit start count
        # 找到确定所求数位所在的数字  该进制位数下第几个数
        num = start + (n - 1) // digit # 2.
        # 确定所求数位在 numnum 的哪一数位
        # n-1 % digit 余数就是这个数的正数第几位
        return int(str(num)[(n - 1) % digit]) # 3.


if __name__ == "__main__":
    pass 