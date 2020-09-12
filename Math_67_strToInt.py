#!/usr/bin/env python 
# encoding: utf-8 

"""
@version: v1.0
@author: zhenglinghan
@contact: 422807471@qq.com
@software: PyCharm
@file: Math_67_strToInt.py
@time: 2020/9/12 23:57
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
    # 考察利用进制，生成10进制数 以及越界问题
    # 2147483647 不记得可以2**31-1 实验一下
    def strToInt(self, str):
        res, i, sign, length = 0, 0, 1, len(str)  # 结果数字 索引 符号 长度
        int_max, int_min, bndry = 2 ** 31 - 1, -2 ** 31, 2 ** 31 // 10# bndry是214748364
        '''
        数字字符：
        字符转数字： “此数字的 ASCII 码” 与 “ 0 的 ASCII 码” 相减即可；
        数字拼接： 若从左向右遍历数字，设当前位字符为 c ，当前位数字为 x，数字结果为 res ，则数字拼接公式为：
        res = 10 * res + x
        x = ascii(c) - ascii('0')
        res=10×res+x
        x=ascii(c)−ascii('0')

        在每轮数字拼接前，判断 res 在此轮拼接后是否超过 2147483647 ，若超过则加上符号位直接返回。
        设数字拼接边界 bndry = 2147483647 // 10 = 214748364，则以下两种情况越界：

        res > bndry & 情况一：执行拼接10×res≥2147483650越界
        res = bndry, x > 7 & 情况二：拼接后是2147483648或2147483649越界

        '''
        if not str:
            return 0  # 空字符串，提前返回
        while str[i] == ' ':
            # 一开始从i开始计数，i之前都为' ' 去除
            i += 1
            if i == length:
                return 0  # 字符串全为空格，提前返回
        # 记录符号
        if str[i] == '-':
            sign = -1
        if str[i] in '+-':
            i += 1
        for c in str[i:]:
            if not '0' <= c <= '9':
                break# 异常！直接返回
            if res > bndry or (res == bndry and c > '7'):
                # 前9位只要>214748364 必然越界
                # 优先级 and 高 其实不用括号
                # 越界
                return int_max if sign == 1 else int_min
            # ord() 函数是 chr() 函数的配对函数 返回一个字符的ascii码
            res = 10 * res + ord(c) - ord('0')
        return sign * res


if __name__ == "__main__":
    s = Solution()
    stri = '-4323431'
    ans = s.strToInt(stri)
    print(ans)
