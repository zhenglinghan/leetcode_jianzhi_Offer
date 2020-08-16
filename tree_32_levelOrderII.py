#!/usr/bin/env python 
# encoding: utf-8 

"""
@version: v1.0
@author: zhenglinghan
@contact: 422807471@qq.com
@software: PyCharm
@file: tree_32_levelOrderII.py
@time: 2020/8/16 20:05
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
    每一层从左到右打印
    '''

    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        self.bfs(root, 0)
        return self.res

    def bfs(self, root, level):
        if not root:
            return
        if level == len(self.res):
            self.res.append([])  # 新的一层
        self.res[level].append(root.val)
        self.bfs(root.left, level + 1)
        self.bfs(root.right, level + 1)


'''
非递归做法
BFS 通常借助 队列 的先入先出特性来实现
每层打印到一行： 将本层全部节点打印到一行，并将下一层全部节点加入队列，以此类推，即可分为多行打印

特例处理： 当根节点为空，则返回空列表 [] ；
初始化： 打印结果列表 res = [] ，包含根节点的队列 queue = [root] ；
BFS 循环： 当队列 queue 为空时跳出；
新建一个临时列表 tmp ，用于存储当前层打印结果；
当前层打印循环： 循环次数为当前层节点数（即队列 queue 长度）；
出队： 队首元素出队，记为 node；
打印： 将 node.val 添加至 tmp 尾部；
添加子节点： 若 node 的左（右）子节点不为空，则将左（右）子节点加入队列 queue ；
将当前层结果 tmp 添加入 res 。
返回值： 返回打印结果列表 res 即可。

'''


class Solution2(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        stack = []
        if not root:
            return []
        else:
            stack.append(root)
        res = []
        while stack:
            tmp = []
            for _ in range(len(stack)):# 这个循环次数是本层一开始的节点数，不会变
                nodei = stack.pop(0)
                tmp.append(nodei.val)
                if nodei.left:
                    stack.append(nodei.left)
                if nodei.right:
                    stack.append(nodei.right)
            res.append(tmp)
        return res


if __name__ == "__main__":
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(2)
    root.left.left = TreeNode(-1)
    root.left.right = TreeNode(9)
    root.left.left.left = TreeNode(0)
    root.right.left = TreeNode(5.1)
    root.right.right = TreeNode(5.2)

    sl = Solution2()
    ans = sl.levelOrder(root)
