#!/usr/bin/env python 
# encoding: utf-8 

"""
@version: v1.0
@author: zhenglinghan
@contact: 422807471@qq.com
@software: PyCharm
@file: Stack_31_validateSrackSequences.py
@time: 2020/9/19 0:44
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
    压栈出栈 如果popped没被全消去，则返回false
    '''

    def validateStackSequences(self, pushed, popped):
        stack = []
        if len(pushed) != len(popped):
            return False
        if pushed and popped:
            for i in range(len(pushed)):
                stack.append(pushed.pop(0))
                while stack and stack[-1] == popped[0]:
                    stack.pop()
                    popped.pop(0)
            if popped:
                return False
            else:
                return True
        else:
            return True


if __name__ == "__main__":
    pass
