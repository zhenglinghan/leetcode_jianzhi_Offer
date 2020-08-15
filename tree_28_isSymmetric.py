#!/usr/bin/env python 
# encoding: utf-8 

"""
@version: v1.0
@author: zhenglinghan
@contact: 422807471@qq.com
@software: PyCharm
@file: tree_28_isSymmetric.py
@time: 2020/8/13 23:31
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
    def isSymmetric(self, root):
        def recur(L, R):
            if not L and not R:  # 一同达到None
                return True
            if not L or not R or L.val != R.val:  # 某一个先达到None 或者出现值不同
                return False
            return L.val == R.val and recur(L.left, R.right) and recur(L.right, R.left)

        return recur(root.left, root.right) if root else True # else True 是空树对称的题目要求


'''
对比子树结构的问题

对称二叉树，树里每个节点下的左右子树都有：
对称二叉树定义： 对于树中 任意两个对称节点 L 和 R ，一定有：
L.val = R.val ：即此两对称节点值相等。
L.left.val = R.right.val ：即 L 的 左子节点 和 R 的 右子节点 对称；
L.right.val = R.left.val ：即 L 的 右子节点 和 R 的 左子节点 对称。
根据以上规律，考虑从顶至底递归，判断每对节点是否对称，从而判断树是否为对称二叉树 一般都递归到叶节点结束

算法流程：
isSymmetric(root) ：

特例处理： 若根节点 root 为空，则直接返回 true 。
返回值： 即 recur(root.left, root.right) ;
recur(L, R) ：

终止条件：
当 L 和 R 同时越过叶节点： 此树从顶至底的节点都对称，因此返回 true ；
当 L 或 R 中只有一个越过叶节点： 此树不对称，因此返回 false ；
当节点 L 值 =/= 节点 R 值： 此树不对称，因此返回 false ；
递推工作：
判断两节点 L.left 和 R.right 是否对称，即 recur(L.left, R.right) ；
判断两节点 L.right 和 R.left 是否对称，即 recur(L.right, R.left) ；
返回值： 两对节点都对称时，才是对称树，因此用与逻辑符 && 连接。

'''

if __name__ == "__main__":
    pass
