#!/usr/bin/env python 
# encoding: utf-8 

"""
@version: v1.0
@author: zhenglinghan
@contact: 422807471@qq.com
@software: PyCharm
@file: tree_27_mirrorTree.py
@time: 2020/8/13 23:13
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
    def mirrorTree(self, root):
        """
        递归法构建镜像二叉树
        时间复杂度 O(N)O(N) ： 其中 NN 为二叉树的节点数量，建立二叉树镜像需要遍历树的所有节点，占用 O(N)O(N) 时间。
        空间复杂度 O(N)O(N) ： 最差情况下（当二叉树退化为链表），递归时系统需使用 O(N)O(N) 大小的栈空间。

        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:# 递归的出口
            return None# 也可以直接return
        tmp = root.left# 难点 递归完下一个root.left = root.right后 root.leftroot.left 的值已经发生改变！
        root.left = self.mirrorTree(root.right)
        root.right = self.mirrorTree(tmp)# root.left还用原先的left
        return root

    def mirrorTree_stack(self, root):
        '''
        利用栈（或队列）遍历树的所有节点 nodenode ，并交换每个 nodenode 的左 / 右子节点。
        :param root:
        :return:
        '''
        if not root:
            return
        stack = [root]# 辅助队列记录下下一层的根 常见的树遍历方式
        while stack:
            node = stack.pop()# 子树的根
            if node.left:
                stack.append(node.left)# 下一层的子树的根
            if node.right:
                stack.append(node.right)# 下一层的子树的根
            node.left, node.right = node.right, node.left# 交换本层！
        return root

if __name__ == "__main__":
    pass 