#!/usr/bin/env python 
# encoding: utf-8 

"""
@version: v1.0
@author: zhenglinghan
@contact: 422807471@qq.com
@software: PyCharm
@file: tree_55_maxDepth.py
@time: 2020/8/18 15:58
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


'''
树的遍历方式总体分为两类：深度优先搜索（DFS）、广度优先搜索（BFS）；

常见的 DFS ： 先序遍历、中序遍历、后序遍历；
常见的 BFS ： 层序遍历（即按层遍历）

'''


class Solution:
    def maxDepth_DFS(self, root):
        if not root:
            return 0
        return max(self.maxDepth_DFS(root.left), self.maxDepth_DFS(root.right)) + 1

    def maxDepth_BFS(self, root):
        if not root:
            return 0
        queue = [root]
        res = 0
        while queue:
            tmp = []
            for index in range(len(queue)):
                nodei = queue[index]
                if nodei.left:
                    tmp.append(nodei.left)
                if nodei.right:
                    tmp.append(nodei.right)
            queue = tmp  # 转移到下一层
            res += 1
        return res


'''
特例处理： 当 root​ 为空，直接返回 深度 00 。
初始化： 队列 queue （加入根节点 root ），计数器 res = 0。
循环遍历： 当 queue 为空时跳出。
初始化一个空列表 tmp ，用于临时存储下一层节点；
遍历队列： 遍历 queue 中的各节点 node ，并将其左子节点和右子节点加入 tmp；
更新队列： 执行 queue = tmp ，将下一层节点赋值给 queue；
统计层数： 执行 res += 1 ，代表层数加 11；
返回值： 返回 res 即可。
'''

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
    print(s.maxDepth_DFS(root))