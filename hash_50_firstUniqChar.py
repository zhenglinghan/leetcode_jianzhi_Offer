#!/usr/bin/env python 
# encoding: utf-8 

"""
@version: v1.0
@author: zhenglinghan
@contact: 422807471@qq.com
@software: PyCharm
@file: hash_50_firstUniqChar.py
@time: 2020/9/3 23:29
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

import collections


class Solution:
    '''
    弱鸡解法 维护一个dict 出现一次就更新一次位置，要是第一次更新就给-1
    找value最小值,如果是-1就返回对应的key，否则认为都出现过1次+
    '''

    def firstUniqChar_0(self, s):
        if not s:
            return " "
        S = {}
        for index, i in enumerate(list(s)):
            if i in S.keys():
                S[i] = index
            else:
                S[i] = -1
        if min(S.values()) == -1:
            return min(S.keys(), key=(lambda k: S[k]))
        else:
            return " "

    def firstUniqChar_1(self, s):
        '''
        高效，true false表示
        :param s:
        :return:
        '''
        dic = {}
        for c in s:
            dic[c] = not c in dic  # c第一次出现
        for c in s:
            if dic[c]:
                # 有break return 不用走完
                return c
        return ' '

    def firstUniqChar_2(self, s):
        '''
        有序哈希表 插入的key有顺序
        :param s:
        :return:
        '''
        dic = collections.OrderedDict()
        for c in s:
            dic[c] = not c in dic
        for k, v in dic.items():# 遍历的是dict 不是s
            if v:
                return k
        return ' '


if __name__ == "__main__":
    pass
