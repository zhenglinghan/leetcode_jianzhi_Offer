#!/usr/bin/env python 
# encoding: utf-8 

"""
@version: v1.0
@author: zhenglinghan
@contact: 422807471@qq.com
@software: PyCharm
@file: other_13_movingcount.py
@time: 2020/9/27 23:59
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

'''
矩阵中的搜索与回溯！
首先只能向右 向下走

决定走一格的整个i+j 数字的大小变化
i+1 进了一个10位 or 没进10位两种请
超出k,总范围，走到已访问就回溯
dfs 递归 1+右搜索所有可行解总数+下方走索的可行解总数
bfs 
'''


class Solution:
    '''
    dfs
    '''

    def movingCount(self, m: int, n: int, k: int) -> int:
        def dfs(i, j, si, sj):
            if i >= m or j >= n or k < si + sj or (i, j) in visited:
                return 0
            visited.add((i, j))
            # 1 + 右方搜索的可达解总数 + 下方搜索的可达解总数
            return 1 + dfs(i + 1, j, si + 1 if (i + 1) % 10 else si - 8, sj) + \
                   dfs(i, j + 1, si, sj + 1 if (j + 1) % 10 else sj - 8)

        visited = set()
        return dfs(0, 0, 0, 0)


class Solution:
    '''
    bfs
    '''

    def movingCount(self, m: int, n: int, k: int) -> int:
        queue, visited, = [(0, 0, 0, 0)], set()# 借用栈替代递归 放入下次要搜索的可行解起点 和坐标位数 像二叉树一样, 已访问
        while queue:
            i, j, si, sj = queue.pop(0)
            if i >= m or j >= n or k < si + sj or (i, j) in visited:
                continue
            visited.add((i, j))
            queue.append((i + 1, j, si + 1 if (i + 1) % 10 else si - 8, sj))
            queue.append((i, j + 1, si, sj + 1 if (j + 1) % 10 else sj - 8))
        return len(visited)
