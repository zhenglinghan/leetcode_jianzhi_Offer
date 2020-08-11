#!/usr/bin/env python 
# encoding: utf-8 

"""
@version: v1.0
@author: zhenglinghan
@contact: 422807471@qq.com
@software: PyCharm
@file: sort_45_minNumber.py
@time: 2020/8/11 21:20
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


class Solution(object):
    '''
    快排解法
    字符串排列的大小推导式子：
    if x+y (xy) >y+x (yx)
       z+y (zy) >y+z (yz)
    则 xz < zx
    具有传递性

    所以只要将2数字a,b排序的比较改成 比较a+b 与 b+a
    若a+b>b+a
    等价于认为b<a
    '''

    def minNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        nums = [str(i) for i in nums]
        # nums = self.qsort(nums)# 递归
        nums = self.qsort_(nums)  # 非递归
        return ''.join(nums)

    def qsort(self, nums):
        if not nums:
            return ['']
        elif len(nums) < 2:
            return [nums[0]]
        else:
            pi = nums[0]
            left = self.qsort([x for x in nums[1:] if x + pi < pi + x])  # 若a+b>b+a 等于 认为 b<a
            right = self.qsort([x for x in nums[1:] if x + pi >= pi + x])
        return left + [pi] + right

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
                if li[high] + pivot < pivot + li[high]:
                    # print('before high2low',li)
                    li[low] = li[high]
                    # 改变布尔值，控制方向
                    high_flag = False
                    low_flag = True
                    # print('after high2low',li)
                else:
                    high -= 1
            if low_flag:
                if li[low] + pivot > pivot + li[low]:
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
    ans = sl.minNumber(['10', '2', '3', '30'])
    print(ans)
