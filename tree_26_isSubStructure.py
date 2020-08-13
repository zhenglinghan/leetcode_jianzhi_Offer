#!/usr/bin/env python 
# encoding: utf-8 

"""
@version: v1.0
@author: zhenglinghan
@contact: 422807471@qq.com
@software: PyCharm
@file: tree_26_isSubStructure.py
@time: 2020/8/13 17:40
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
    def check(self, s, t):  # 这里 t 可能为空
        #  B 属于 A 的一部分也可以，没必要一直匹配到叶子节点
        # 此部分只要B树达到None即可
        if not t:
            return True
        if not s:
            return False
        return s.val == t.val and self.check(s.left, t.left) and self.check(s.right, t.right)

    def isSubStructure(self, A, B):

        if not A or not B: return False
        return self.check(A, B) or self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B)


'''
所有树结构匹配的方法 递归 总结：
1：dfs 到两者同时达到None
2: 递归根节点，检查A左与B,检查A右与B
'''


class Solution_treeMatch(object):
    def dfs(self, s, t):
        if not t and not s:  # 一同达到None
            return True
        if not s or not t:  # 某一个先达到None
            return False
        return s.val == t.val and self.check(s.left, t.left) and self.check(s.right, t.right)

    def isSubStructure(self, A, B):

        if not A or not B: return False
        return self.check(A, B) or self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B)


if __name__ == "__main__":
    a = TreeNode(0)
    a.left = TreeNode(1)
    a.left.left = TreeNode(2)
    a.left.left.left = TreeNode(3)
    a.left.left.right = TreeNode(4)
    a.right = TreeNode(5)

    b = TreeNode(2)
    b.left = TreeNode(3)
    b.right = TreeNode(4)

    c = TreeNode(1)
    c.left = TreeNode(2)
    c.right = TreeNode(2.5)
    c.left.left = TreeNode(3)
    c.left.right = TreeNode(4)

    sl = Solution()
    ans1 = sl.isSubStructure(a, b)
    print(ans1)
    ans1 = sl.isSubStructure(a, c)
    print(ans1)
