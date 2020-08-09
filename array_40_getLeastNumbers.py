#!/usr/bin/env python 
# encoding: utf-8 

"""
@version: v1.0
@author: zhenglinghan
@contact: 422807471@qq.com
@software: PyCharm
@file: array_40_getLeastNumbers.py
@time: 2020/8/9 23:26
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
    def getLeastNumbers(self, arr, k):
        if k == 0:
            return []
        heaplist = HeapList()
        heaplist.buildHeap(arr[:k])
        for i in arr[k:]:
            if i < heaplist.heaplist[1]:
                heaplist.delMax()
                heaplist.insert(i)
        return heaplist.heaplist[1:]


class HeapList():
    """
    大顶堆
    """

    def __init__(self):
        self.heaplist = [0]
        self.size = 0

    def buildHeap(self, alist):
        i = len(alist) // 2
        self.size = len(alist)
        self.heaplist += alist[:]
        while i > 0:
            self.percDown(i)
            i -= 1

    def delMax(self):
        """删除堆顶最大元素"""
        retval = self.heaplist[1]
        self.heaplist[1] = self.heaplist[self.size]
        self.size -= 1
        self.heaplist.pop()
        self.percDown(1)
        return retval

    def insert(self, k):
        self.heaplist.append(k)
        self.size += 1
        self.percUP(self.size)

    def percUP(self, i):
        while i // 2 > 0:
            if self.heaplist[i] > self.heaplist[i // 2]:
                self.heaplist[i], self.heaplist[i // 2] = self.heaplist[i // 2], self.heaplist[i]
            i //= 2

    def percDown(self, i):
        while i * 2 <= self.size:
            mc = self.maxChild(i)
            if self.heaplist[i] < self.heaplist[mc]:
                self.heaplist[i], self.heaplist[mc] = self.heaplist[mc], self.heaplist[i]
            i = mc

    def maxChild(self, i):
        if 2 * i + 1 > self.size:
            return 2 * i
        else:
            if self.heaplist[2 * i] > self.heaplist[2 * i + 1]:
                return 2 * i
            else:
                return 2 * i + 1

class Solution1:
    def getLeastNumbers(self, arr, k: int):
        arr.sort()
        return arr[:k]


class Solution2:
    def getLeastNumbers(self, arr, k):
        def partition(arr, l, r):
            # 选定中值
            pivotvalue = arr[l]
            lmark = l + 1
            rmark = r
            done = False

            while not done:
                while lmark <= rmark and arr[lmark] <= pivotvalue:
                    lmark += 1
                while rmark >= lmark and arr[rmark] >= pivotvalue:
                    rmark -= 1
                if rmark < lmark:
                    done = True
                else:
                    arr[lmark], arr[rmark] = arr[rmark], arr[lmark]

            arr[l], arr[rmark] = arr[rmark], arr[l]
            return rmark

        def quicksort(arr, l, r, k):
            if l > r:
                return
            pos = partition(arr, l, r)
            num = pos - l + 1
            if k == num:
                return
            if k < num:
                quicksort(arr, l, pos - 1, k)
            else:
                quicksort(arr, pos + 1, r, k - num)

        if k == 0:
            return []
        quicksort(arr, 0, len(arr) - 1, k)
        return arr[:k]

if __name__ == "__main__":
    sl = Solution()
    ans = sl.getLeastNumbers([1, 4, 5, 1, 3, 5, 2], 3)
    print(ans)
