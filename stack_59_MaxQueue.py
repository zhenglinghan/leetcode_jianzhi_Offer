#!/usr/bin/env python 
# encoding: utf-8 

"""
@version: v1.0
@author: zhenglinghan
@contact: 422807471@qq.com
@software: PyCharm
@file: stack_59_MaxQueue.py
@time: 2020/8/7 0:22
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


class MaxQueue(object):

    def __init__(self):
        self.queueA = []  # 维护的递减序列
        self.queueB = []  # 存数序列

    def max_value(self):
        """
        :rtype: int
        """
        # 返回这个序列的头部【0】 就可以
        return self.queueA[0] if self.queueA else -1

    def push_back(self, value):
        """
        :type value: int
        :rtype: None
        """
        # 当放入的数比queueA 头部大就从头部取出数，指导留下比新的数更大的数
        # 这样数列就是递减的（【-1】是尾部最大 【0】是头部最小）
        while self.queueA and self.queueA[-1] < value:
            self.queueA.pop()
        # 新的数字放入
        self.queueA.append(value)
        self.queueB.append(value)

    def pop_front(self):
        """
        :rtype: int
        """
        if not self.queueA:
            return -1
        # 取出最大的【-1】尾部
        ans = self.queueB.pop(0)
        # 容易错
        # 如果取出的值是维护队列queueA中最小的，也取出
        if ans == self.queueA[0]:
            self.queueA.pop(0)
        return ans


# Your MaxQueue object will be instantiated and called as such:
# obj = MaxQueue()
# param_1 = obj.max_value()
# obj.push_back(value)
# param_3 = obj.pop_front()



if __name__ == "__main__":
    '''
    ["MaxQueue","push_back","push_back","max_value","pop_front","max_value"]
[[],[1],[2],[],[],[]]
    '''
    obj = MaxQueue()
    obj.push_back(3)
    obj.push_back(2)
    param_1 = obj.max_value()
    obj.pop_front()
    param_3 = obj.max_value()
    print(param_1, param_3)
