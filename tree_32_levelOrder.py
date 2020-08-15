#!/usr/bin/env python 
# encoding: utf-8 

"""
@version: v1.0
@author: zhenglinghan
@contact: 422807471@qq.com
@software: PyCharm
@file: tree_32_levelOrder.py
@time: 2020/8/15 23:46
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
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # 循环操作一般都要用到stack
        if root is None:
            return []
        if root.left is None and root.right is None:
            return [root.val]
        stack = [root]
        output = []
        '''
        可以借助队列先进先出的特点，
        ①每次取对头节点的值放入结果中
        ②按照先序遍历每次先将根节点存入，再依次存入其左孩子右孩子（如果有的话）
        以上两点在while循环中实现，直至队列长度为0
        '''
        while (stack):  # 下一层要打印的根
            for i in range(len(stack)):
                out_node = stack.pop(0)  # 先进先出
                output.append(out_node.val)
                if out_node.left is not None:
                    stack.append(out_node.left)  # 这个头结点的左孩子 放入下一层要打印的stack里
                if out_node.right is not None:
                    stack.append(out_node.right)  # 这个头结点的右孩子 放入下一层要打印的stack里
        return output


if __name__ == "__main__":
    pass
