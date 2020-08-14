#!/usr/bin/env python 
# encoding: utf-8 

"""
@version: v1.0
@author: zhenglinghan
@contact: 422807471@qq.com
@software: PyCharm
@file: tree_28_isSymmetric.py
@time: 2020/8/13 23:31
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


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isSymmetric(self, root):
        def recur(L, R):
            if not L and not R:  # 一同达到None
                return True
            if not L or not R or L.val != R.val:  # 某一个先达到None 或者出现值不同
                return False
            return L.val == R.val and recur(L.left, R.right) and recur(L.right, R.left)

        return recur(root.left, root.right) if root else True

'''
对比子树结构的问题

'''

if __name__ == "__main__":
    pass
