#!/usr/bin/env python 
# encoding: utf-8 

"""
@version: v1.0
@author: zhenglinghan
@contact: 422807471@qq.com
@software: PyCharm
@file: ListNode_06_reversePrint.py
@time: 2020/9/9 23:59
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


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # def reversePrint(self, head):
    #     stack = []
    #     while head:
    #         stack.append(head.val)
    #         head = head.next
    #     return stack[::-1]
    def reversePrint(self, head):
        return self.reversePrint(head.next) + [head.val] if head else []

if __name__ == "__main__":
    pass 