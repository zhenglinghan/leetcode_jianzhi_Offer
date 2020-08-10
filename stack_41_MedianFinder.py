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


class MedianFinder1(object):
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


from heapq import *

class MedianFinder(object):
    '''
    使用大根堆和小根堆
    假想我们现在有两个容器 A, B 这两个容器将我们的整体数据分成两部分,且 A 中的数据都小于 B 中的数据,并且 A 中的最后一个数据是 A 里面最大的B 的第一个数据是 B 中最小的.
    好了 我们有了上面的条件,那我们怎么找到中位数呢?
    当整体数目为奇数时,中间的那个数就是所求.当整体数目为偶数时,中间两个数的和再除以 2 ,就能得到结果
    我们只要将上面的两个容器的数据数目只差保持在 1 之内即可,也就是说 A 和 B 将整体数据以中位数划分开来了
    '''
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.bigHpeap = []
        self.smallHeap = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        if len(self.bigHpeap) == len(self.smallHeap):  # 总数为偶数时,先插入到大根堆,在插入到小根堆
            heappush(self.smallHeap, -heappushpop(self.bigHpeap, -num))
        else:  # 总数为奇数时,先插入到小根堆,在插入到大根堆
            heappush(self.bigHpeap, -heappushpop(self.smallHeap, num))

    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.bigHpeap) == len(self.smallHeap):
            return (-self.bigHpeap[0] + self.smallHeap[0]) / 2.0
        else:
            return self.smallHeap[0]

# heapq:
'''

heapq 模块提供了堆算法。heapq是一种子节点和父节点排序的树形数据结构。
这个模块提供heap[k] <= heap[2*k+1] and heap[k] <= heap[2*k+2]。为了比较不存在的元素被人为是无限大的。heap最小的元素总是[0]

方法heappush
heap = []
heapq.heappush(heap, i)
根据结果可以了解，子节点的元素大于父节点元素。而兄弟节点则不会排序。

方法heapq.heapify(list)
将list类型转化为heap, 在线性时间内, 重新排列列表

方法删除并返回堆中最小的元素, 通过heapify() 和heappop()来排序

方法heapq.heapreplace(iterable, n)
删除现有元素并将其替换为一个新值

方法heapq.nlargest(n, iterable) 和 heapq.nsmallest(n, iterable)

'''

if __name__ == "__main__":
    mf = MedianFinder1()
    arr = [1, 4, 5, 9, 13, 14, 15, 19, 20]
    for i in arr[::-1]:
        mf.addNum(i)
    print(mf.arr)
    print(mf.findMedian())

    mf = MedianFinder()
    arr = [1, 4, 5, 9, 13, 14, 15, 19, 20]
    for i in arr[::-1]:
        mf.addNum(i)
    print(mf.smallHeap, mf.bigHpeap)
    print(mf.findMedian())
