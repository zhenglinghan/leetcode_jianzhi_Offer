#!/usr/bin/env python 
# encoding: utf-8 

"""
@version: v1.0
@author: zhenglinghan
@contact: 422807471@qq.com
@software: PyCharm
@file: stack_09_CQueue.py
@time: 2020/8/5 23:32
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

# 栈结构基础 后进先出 top 表示尾部最上方 会先出来 end表示底部 最后出
# class Stack(object):
#     def __init__(self):
#         self.stack = []
#
#     def push(self, value):    # 进栈
#         self.stack.append(value)
#
#     def pop(self):  #出栈
#         if self.stack:
#             self.stack.pop()
#         else:
#             raise LookupError('stack is empty!')
#
#     def is_empty(self): # 如果栈为空
#         return bool(self.stack)
#
#     def top(self):
#         #取出目前stack中最新的元素
#         return self.stack[-1]

class CQueue:
    def __init__(self):
        self.A, self.B = [], []

    def appendTail(self, value):
        self.A.append(value)

    def deleteHead(self):
        if self.B:
            return self.B.pop()
        if not self.A:
            return -1
        while self.A:
            self.B.append(self.A.pop())# A弹出来到B 完成逆序 然后删除pop 出B的top
        return self.B.pop()


if __name__ == "__main__":
    cq = CQueue()
    cq.appendTail(5)
    cq.appendTail(6)
    cq.appendTail(7)
    paramsCQ = cq.deleteHead()
    print(paramsCQ)
