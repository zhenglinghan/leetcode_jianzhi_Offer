#!/usr/bin/env python 
# encoding: utf-8 

"""
@version: v1.0
@author: zhenglinghan
@contact: 422807471@qq.com
@software: PyCharm
@file: tree_34_pathSum.py
@time: 2020/8/16 23:20
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
    def __init__(self):
        self.res, self.path = [], []

    def pathSum(self, root, tar):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        self.recur(root, tar)
        return self.res

    def recur(self, root, tar):
        if not root:
            return# 走完到底叶子节点的left or right 都是None
        # 先序遍历
        self.path.append(root.val)  # 根
        tar -= root.val
        if tar == 0 and not root.left and not root.right:  # 路径走完，和等于目标值
            self.res.append(self.path.copy()) # 难点 path内容会变
        self.recur(root.left, tar)
        self.recur(root.right, tar)
        self.path.pop()  # ?
        # 理解路径恢复： 向上回溯前，需要将当前节点从路径 path 中删除，即执行 path.pop()


if __name__ == "__main__":
    pass
