#!/usr/bin/env python 
# encoding: utf-8 

"""
@version: v1.0
@author: zhenglinghan
@contact: 422807471@qq.com
@software: PyCharm
@file: tree_32_levelOrderIII.py
@time: 2020/8/16 20:49
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


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def __init__(self):
        self.res = []

    '''
    BFS 遍历
    以level变量控制层级
    每一层一个list 从level 0开始
    当level等于当前len时便新增一个list存下一层的数据
    奇数层从左到右打印
    偶数层从右到左打印
    '''

    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        self.bfs(root, 0)
        return self.res

    '''
        非递归
    '''
    def bfs(self, root, level):
        if not root:
            return
        if level == len(self.res):
            self.res.append([])  # 新的一层
        if level % 2:
            # level 1是第二行，已经要从右向左了
            self.res[level] = [root.val] + self.res[level]
        else:
            self.res[level].append(root.val)
        self.bfs(root.left, level + 1)
        self.bfs(root.right, level + 1)


if __name__ == "__main__":
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(2)
    root.left.left = TreeNode(-1)
    root.left.right = TreeNode(9)
    root.left.left.left = TreeNode(0)
    root.right.left = TreeNode(5.1)
    root.right.right = TreeNode(5.2)

    sl = Solution()
    ans = sl.levelOrder(root)
    print(ans)
