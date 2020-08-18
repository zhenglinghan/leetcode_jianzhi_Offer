#!/usr/bin/env python 
# encoding: utf-8 

"""
@version: v1.0
@author: zhenglinghan
@contact: 422807471@qq.com
@software: PyCharm
@file: tree_55_isBalanced.py
@time: 2020/8/18 17:35
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
    def isBalanced(self, root):
        def recur(root):
            if not root:  # 出口
                return 0  # 正常递归穿过叶子节点 作为递归到底部叶子节点 开始计算深度 从0开始 特例空树也在这里
            left = recur(root.left)
            if left == -1:  # 出口
                return -1
            right = recur(root.right)
            if right == -1:  # 出口
                return -1
            return max(left, right) + 1 if abs(left - right) <= 1 else -1

        return recur(root) != -1


if __name__ == "__main__":
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(2)
    root.left.left = TreeNode(-1)
    root.left.right = TreeNode(9)
    root.left.left.left = TreeNode(0)
    root.right.left = TreeNode(5.1)
    root.right.right = TreeNode(5.2)

    s = Solution()
    print(s.isBalanced(root))
