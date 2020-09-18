#!/usr/bin/env python 
# encoding: utf-8 

"""
@version: v1.0
@author: zhenglinghan
@contact: 422807471@qq.com
@software: PyCharm
@file: String_67_strToInt.py
@time: 2020/9/19 0:02
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
    def strToInt(self, str: str) -> int:
        res, i, sign, length = 0, 0, 1, len(str)  # 结果数字 索引 符号 长度
        int_max, int_min, bndry = 2 ** 31 - 1, -2 ** 31, 2 ** 31 // 10
        '''
        在每轮数字拼接前，判断 res 在此轮拼接后是否超过 2147483647 ，若超过则加上符号位直接返回。
        设数字拼接边界 bndry = 2147483647 // 10 = 214748364，则以下两种情况越界：

        res > bndry & 情况一：执行拼接10×res≥2147483650越界
        res = bndry, x > 7 & 情况二：拼接后是2147483648或2147483649越界

        '''
        if not str:
            return 0  # 空字符串，提前返回
        while str[i] == ' ':
            i += 1
            if i == length:
                return 0  # 字符串全为空格，提前返回
        if str[i] == '-':
            sign = -1
        if str[i] in '+-':
            i += 1
        for c in str[i:]:
            if not '0' <= c <= '9': break
            if res > bndry or (res == bndry and c > '7'):
                return int_max if sign == 1 else int_min
            res = 10 * res + ord(c) - ord('0')
        return sign * res


if __name__ == "__main__":
    pass 