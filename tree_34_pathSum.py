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


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


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
            return  # 走完到底叶子节点的left or right 都是None
        # 先序遍历
        self.path.append(root.val)  # 根
        tar -= root.val
        if tar == 0 and not root.left and not root.right:  # 路径走完，和等于目标值
            self.res.append(self.path.copy())  # 难点 path内容会变
        self.recur(root.left, tar)
        self.recur(root.right, tar)
        self.path.pop()  #
        # 理解路径恢复： 向上回溯前，需要将当前节点从路径 path 中删除，即执行 path.pop()
        # 路径走到底，必须pop回到根节点走另一侧。。所以要有pop


if __name__ == "__main__":
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(8)
    root.left.left = TreeNode(11)
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(2)
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(4)
    root.right.right.left = TreeNode(5)
    root.right.right.right = TreeNode(1)

    sl = Solution()
    ans = sl.pathSum(root, 20)
