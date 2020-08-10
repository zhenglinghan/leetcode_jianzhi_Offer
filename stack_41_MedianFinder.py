#!/usr/bin/env python 
# encoding: utf-8 

"""
@version: v1.0
@author: zhenglinghan
@contact: 422807471@qq.com
@software: PyCharm
@file: stack_41_MedianFinder.py
@time: 2020/8/10 22:41
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


class MedianFinder(object):
    '''
    通过二分查找维护保序队列执行用时： 2416 ms  内存消耗：24.9 MB
    '''
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.arr = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        self.arr = self.binary_insert(self.arr, num)

    def binary_search(self, list_item, item):
        """
        list_item
        item item要插入到保序队列的位置
        返回位置
        """
        low = 0
        high = len(list_item)
        while low < high:
            mid = int((low + high) / 2)
            guess = list_item[mid]
            if guess == item:
                return mid
            if item < guess:
                high = mid
            else:
                low = mid + 1
        return high

    def binary_insert(self, list_item, item):
        """
        list_item
        item item要插入到保序队列的位置
        """
        # 没必要.pop...
        pindex = self.binary_search(list_item, item)
        # 切片
        list_item = list_item[:pindex] + [item] + list_item[pindex:]
        return list_item

    def findMedian(self):
        """
        :rtype: float
        """
        n = len(self.arr)
        if n & 1 == 1:  # n是奇数
            return self.arr[n // 2]
        else:
            return (self.arr[n // 2] + self.arr[n // 2 - 1]) / 2


if __name__ == "__main__":
    mf = MedianFinder()
    arr = [1, 4, 5, 9, 13, 14, 15, 19, 20]
    # item = 7
    # index = mf.binary_search(arr,item)
    for i in arr[::-1]:
        mf.addNum(i)
    print(mf.arr)
    print(mf.findMedian())
