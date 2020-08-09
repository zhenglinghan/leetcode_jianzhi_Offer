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


class Solution3:
    def getLeastNumbers(self, arr, k):
        arr = self.qsort(arr)
        return arr[:k]
    def qsort(self, arr):
        if not len(arr):
            return []
        else:
        # 在这里以第一个元素为基准线
            pivot = arr[0]
            left = self.qsort([x for x in arr[1:] if x < pivot])
            right = self.qsort([x for x in arr[1:] if x >= pivot])
        return left+[pivot]+right

class Solution4:
    def getLeastNumbers(self, arr, k):
        arr = self.qsort_(arr)
        return arr[:k]

    def qsort_(self, arr):
        '''''
       模拟栈操作实现非递归的快速排序
       '''
        if len(arr) < 2:
            return arr
        stack = []
        stack.append(len(arr) - 1)  # 队尾入栈
        stack.append(0)  # 队首入栈
        while stack:
            # 第二次迭代中等于取出上一次分区中的右分区的队尾队首index进行再次partition操作
            # 然后先对右边的分区不断迭代做递归存index 到stack里 弹出 直到右边分区顺序
            # 然后开始弹出左边分区 不断迭代做递归 直到左边分区顺序正常
            l = stack.pop()  # 当前栈中的 分区队首出栈
            r = stack.pop()  # 分区队尾出栈
            index = self.partition(arr, l, r)  # 返回 分区后的数组 比基准值小的在左边，+基准值+右边
            if l < index - 1:
                stack.append(index - 1)  # 左分区队尾入栈
                stack.append(l)  # 左分区队首入栈
            if r > index + 1:
                stack.append(r)  # 右分区队尾入栈
                stack.append(index + 1)  # # 右分区队首入栈
        return arr

    def partition(self, li, low, high):
        # 这个函数是用来找出确定值的索引
        # 首先设置俩个布尔变量，通过这个来控制左右移动
        high_flag = True
        low_flag = False
        # 将开始位置的值定为基数
        pivot = li[low]
        while low < high and low < len(li) and high < len(li):
            # 当这个值为真时，游标从右开始移动
            if high_flag:
                # 找出右边比基数小的值，互换位置，否则一直向右移动
                if li[high] < pivot:
                    # print('before high2low',li)
                    li[low] = li[high]
                    # 改变布尔值，控制方向
                    high_flag = False
                    low_flag = True
                    # print('after high2low',li)
                else:
                    high -= 1
            if low_flag:
                if li[low] > pivot:
                    # print('before low2high',li)
                    li[high] = li[low]
                    high_flag = True
                    low_flag = False
                    # print('after low2high',li)
                else:
                    low += 1
        li[low] = pivot  # 基准值放如list中间位置
        # 返回的是索引位置 单list顺序已经被分为了左队列 基准值 右队列
        return low
if __name__ == "__main__":
    sl = Solution()
    ans = sl.getLeastNumbers([1, 4, 5, 1, 3, 5, 2], 3)
    print(ans)
