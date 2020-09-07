#!/usr/bin/env python 
# encoding: utf-8 

"""
@version: v1.0
@author: zhenglinghan
@contact: 422807471@qq.com
@software: PyCharm
@file: ListNode_18_deleteNode.py
@time: 2020/9/7 23:52
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


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    '''
    双指针定位用遍历，跳开next就是删除
    继续遍历
    node2 = node1
    node1 = node1.next
    '''
    def deleteNode(self, head, val):
        if head.val == val:
            return head.next
        node1 = head.next  # cur
        node2 = head  # pre
        while 1:
            if node1.val == val or node1.val == None:
                node2.next = node1.next
                return head
            else:
                node2 = node1
                node1 = node1.next


if __name__ == "__main__":
    pass
