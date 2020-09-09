#!/usr/bin/env python 
# encoding: utf-8 

"""
@version: v1.0
@author: zhenglinghan
@contact: 422807471@qq.com
@software: PyCharm
@file: ListNode_22_getKthFromEnd.py
@time: 2020/9/9 23:55
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
    def getKthFromEnd(self, head, k):
        '''
        双指针 不用记录链表长度 前者触底，返回后者
        :param head:
        :param k:
        :return:
        '''
        pre = head
        post = head
        for i in range(k):
            pre = pre.next
        while pre != None:
            pre = pre.next
            post = post.next
        return post


if __name__ == "__main__":
    pass
