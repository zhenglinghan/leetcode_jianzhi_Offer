#!/usr/bin/env python 
# encoding: utf-8 

"""
@version: v1.0
@author: zhenglinghan
@contact: 422807471@qq.com
@software: PyCharm
@file: tree_68_lowestCommonAncestor.py
@time: 2020/8/18 23:36
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
方法一：迭代
循环搜索： 当节点 root 为空时跳出；
当 p, q 都在 root 的 右子树 中，则遍历至 root.right ；
否则，当 p, q 都在 root 的 左子树 中，则遍历至 root.left ；
否则，说明找到了 最近公共祖先 ，跳出。
返回值： 最近公共祖先 root 。

方法二：递归
递推工作：
当 p, q都在 root 的 右子树 中，则开启递归 root.right 并返回；
否则，当 p, q 都在 root 的 左子树 中，则开启递归 root.left 并返回；
返回值： 最近公共祖先 root 。
'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    '''
    循环解法
    '''

    def lowestCommonAncestor(self, root, p, q):
        if p.val > q.val:
            p, q = q, p  # 保证 p.val < q.val # 优化条件判断
        while root:
            if root.val < p.val:  # p,q 都在 root 的右子树中
                root = root.right  # 遍历至右子节点
            elif root.val > q.val:  # p,q 都在 root 的左子树中
                root = root.left  # 遍历至左子节点
            else:
                break
        return root

    '''
    递归解法
    '''

    def lowestCommonAncestor_2(self, root, p, q):
        if root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        if root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        return root


if __name__ == "__main__":
    pass
