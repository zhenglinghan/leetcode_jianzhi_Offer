#!/usr/bin/env python 
# encoding: utf-8 

"""
@version: v1.0
@author: zhenglinghan
@contact: 422807471@qq.com
@software: PyCharm
@file: String_05_replaceSpace.py
@time: 2020/9/20 23:58
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
    尽量做到 时间O(N) 空间O(1)
    '''
    def replaceSpace(self, s: str) -> str:
        i = 0
        while i<len(s):
            if s[i]==' ':
                s = s[:i]+'%20'+s[i+1:]
                i+=3
            else:
                i+=1
        return s


if __name__ == "__main__":
    pass 