#!/usr/bin/env python 
# encoding: utf-8 

"""
@version: v1.0
@author: zhenglinghan
@contact: 422807471@qq.com
@software: PyCharm
@file: tree_26_treeToDoublyList.py
@time: 2020/9/28 16:53
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


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        '''
        当前被访问的节点的指针：cur
        '''

        def dfs(cur):
            if not cur:
                return
            dfs(cur.left)  # 递归左子树
            if self.pre:  # 修改节点引用pre是全局的指针 回溯出来的cur 是pre的下一个节点 要建立连接了
                self.pre.right, cur.left = cur, self.pre  # 做成双向
            else:  # 记录头节点
                self.head = cur  # pre是none则出现头结点 放入全局
            self.pre = cur  # 保存 cur # 最先保存的是头结点 从头结点开始->尾部
            dfs(cur.right)  # 递归右子树

        if not root:  # 特例
            return
        self.pre = None
        dfs(root)# 结束后self.pre是 root
        self.head.left, self.pre.right = self.pre, self.head
        return self.head  # 返回头


if __name__ == "__main__":
    a = Node(5)
    b = Node(10)
    c = Node(15)
    d = Node(20)
    e = Node(25)
    b.right = c
    b.left = a
    d.left = b
    d.rigth = e
    s = Solution()
    head = s.treeToDoublyList(d)
