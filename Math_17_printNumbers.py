#!/usr/bin/env python 
# encoding: utf-8 

"""
@version: v1.0
@author: zhenglinghan
@contact: 422807471@qq.com
@software: PyCharm
@file: Math_17_printNumbers.py
@time: 2020/9/17 14:30
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


# class Solution:
#     '''
#     考虑打印字符串 避免大数问题
#     规则是每一个10进制位上都0~9出现一遍，先出现完下一个位的0~9
#     等价于n个位，做全排列，注意顺序
#     考虑放入数组的num 有几个0
#     生成数据，有前后递进关系变量（digit） 可以用递归
#     '''
#
#     def printNumbers(self, n):
#         def dfs(x):
#             if x == n:  # 终止条件：已固定完所有位
#                 res.append(''.join(num))  # 拼接 num 并添加至 res 尾部
#                 return
#             for i in range(10):  # 遍历 0 - 9
#                 num[x] = str(i)  # 固定第 x 位为 i
#                 dfs(x + 1)  # 开启固定第 x + 1 位
#
#         num = ['0'] * n  # 起始数字定义为 n 个 0 组成的字符列表
#         res = []  # 数字字符串列表
#         dfs(0)  # 开启全排列递归
#         return ','.join(res)  # 拼接所有数字字符串，使用逗号隔开，并返回
#
#     def printNumbers_self(self, n):
#         '''
#         递推公式：
#         dfs
#         :param n:
#         :return:
#         '''
#         def dfs(x):
#             if x == n:
#                 res.append(''.join(num))
#             return
#             for i in range(10):
#                 num[x] = str(i)
#                 dfs(x + 1)

# num = ['0'] * n#起始数字
# res = []# 数字字符串
# dfs(0)
# return ','.join(res)

# 先固定高位，向低位递归
# 递推公式：
# dfs(n) = dfs(n-1) + 一个已经被固定住的高位
# class Solution:
#     def printNumbers(self, n):
#         def dfs(x):
#             if x == n:
#                 s = ''.join(num[self.start:])
#                 if s != '0':
#                     res.append(s)
#                 if n - self.start == self.nine:
#                     self.start -= 1
#                 return
#             for i in range(10):
#                 if i == 9:
#                     self.nine += 1
#                 num[x] = str(i)
#                 dfs(x + 1)
#             self.nine -= 1  # 下一轮时还要恢复
#
#         num, res = ['0'] * n, []
#         self.nine = 0  # 是都排列完一次9 ，就+1
#         self.start = n - 1  # 每排列完0~9 就在下次放入的时候多保留一位
#         dfs(0)
#         return ','.join(res)


class Solution2:
    def printNumbers(self, n):
        def dfs(x):
            if x == n:
                res.append(''.join(num))
                return
            for i in range(10):
                num[x] = str(i)
                dfs(x+1)

        num, res = ['0'] * n, []
        dfs(0)
        return ','.join(res)


if __name__ == "__main__":
    N = 3
    # S = Solution()
    # print(S.printNumbers(N))

    S = Solution2()
    ans = S.printNumbers(N)
    print(ans)
