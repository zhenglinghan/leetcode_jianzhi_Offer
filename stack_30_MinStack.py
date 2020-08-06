#!/usr/bin/env python 
# encoding: utf-8 

"""
@version: v1.0
@author: zhenglinghan
@contact: 422807471@qq.com
@software: PyCharm
@file: stack_30_MinStack.py
@time: 2020/8/6 23:46
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


class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stackI = []
        self.stackJ = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stackI.append(x)
        if not self.stackJ or x <= self.stackJ[-1]:
            self.stackJ.append(x)

    def pop(self):
        """
        :rtype: None
        """
        assert self.stackI
        if self.stackI[-1] == self.stackJ[-1]:
            self.stackJ.pop()
        return self.stackI.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stackI[-1]

    def min(self):
        """
        :rtype: int
        """
        # min(self.stackI)
        return self.stackJ[-1]

# 空间换时间
# min(self.stackI) 时间复杂度O(N)

# 维护一个最小值的栈
# 保证数据一致即可 容易错的是if not self.stackJ or x <= self.stackJ[-1]: x要小于等于，只要有同等小的值就要一并加入
# 复习下assert True  复习下raise if not

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.min()


if __name__ == "__main__":
    obj = MinStack()
    obj.push(1)
    obj.push(2)
    obj.push(1)
    print(obj.min())
    obj.pop()
    param_3 = obj.top()
    param_4 = obj.min()
    print(param_3, param_4)