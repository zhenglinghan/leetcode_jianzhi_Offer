#!/usr/bin/env python 
# encoding: utf-8 

"""
@version: v1.0
@author: zhenglinghan
@contact: 422807471@qq.com
@software: PyCharm
@file: tree_07_buildTree.py
@time: 2020/8/12 18:21
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
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """


class Solution_tree_built(object):
    def buildTree_pre_in(self, preorder, inorder):
        """
        前序 中序恢复整颗树
        :param preorder:
        :param inorder:
        :return:
        """
        if not preorder or not inorder:
            return None
        '''
        前序  根 左 右
        中序  左 根 右
        后序  左 右 根
        '''
        root = TreeNode(preorder.pop(0))  # 前序遍历第一个点作为根 取出
        indexroot = inorder.index(root.val)  # 这个跟的子树的访问顺序里中序为左 + 根 +右，找到根的位置
        root.left = self.buildTree_pre_in(preorder, inorder[:indexroot])  # 对于根的左边子树仍然做一个根据前序，中序 重建的过程
        root.right = self.buildTree_pre_in(preorder, inorder[indexroot + 1:])  # 对于根的右边子树仍然做一个根据前序，中序 重建的过程
        return root  # 返回根节点代表这颗子树

    def buildTree_pre_last(self, preorder, lastorder):
        """
        前序 后序恢复整颗树
        :param preorder:
        :param inorder:
        :return:
        """
        if not preorder or not lastorder:
            return None
        '''
        前序  根 左 右
        中序  左 根 右
        后序  左 右 根
        '''
        root = TreeNode(preorder.pop(0))  # 前序遍历第一个点作为根 取出
        indexroot = lastorder.index(root.val)  # 这个跟的子树的访问顺序里中序为左 + 根 +右，找到根的位置
        root.left = self.buildTree_pre_in(preorder, lastorder[:indexroot])  # 对于根的左边子树仍然做一个根据前序，中序 重建的过程
        root.right = self.buildTree_pre_in(preorder, lastorder[indexroot + 1:])  # 对于根的右边子树仍然做一个根据前序，中序 重建的过程
        return root  # 返回根节点代表这颗子树

    def buildTree_in_last(self, preorder, lastorder):
        """
        中序 后序恢复整颗树
        :param preorder:
        :param inorder:
        :return:
        """
        if not preorder or not lastorder:
            return None
        '''
        前序  根 左 右
        中序  左 根 右
        后序  左 右 根
        '''
        root = TreeNode(preorder.pop(0))  # 前序遍历第一个点作为根 取出
        indexroot = lastorder.index(root.val)  # 这个跟的子树的访问顺序里中序为左 + 根 +右，找到根的位置
        root.left = self.buildTree_pre_in(preorder, lastorder[:indexroot])  # 对于根的左边子树仍然做一个根据前序，中序 重建的过程
        root.right = self.buildTree_pre_in(preorder, lastorder[indexroot + 1:])  # 对于根的右边子树仍然做一个根据前序，中序 重建的过程
        return root  # 返回根节点代表这颗子树


def PrintTree(pRoot):
    '''
    按层从左到右打印tree
    :param pRoot:
    :return:
    '''
    # 循环操作一般都要用到stack
    if pRoot is None:
        return []
    if pRoot.left is None and pRoot.right is None:
        return [[pRoot.val]]
    stack = [pRoot]
    output = []
    '''
    可以借助队列先进先出的特点，
    ①每次取对头节点的值放入结果中
    ②按照先序遍历每次先将根节点存入，再依次存入其左孩子右孩子（如果有的话）
    以上两点在while循环中实现，直至队列长度为0
    '''
    while (stack):  # 下一层要打印的根
        temp = []
        for i in range(len(stack)):
            out_node = stack.pop(0)  # 先进先出
            temp.append(out_node.val)
            if out_node.left is not None:
                stack.append(out_node.left)  # 这个头结点的左孩子 放入下一层要打印的stack里
            if out_node.right is not None:
                stack.append(out_node.right)  # 这个头结点的右孩子 放入下一层要打印的stack里
        output.append(temp)
    return output


# 3种递归遍历树的方式
def preorderTraversal(root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    if not root:
        return []
    return [root.val] + preorderTraversal(root.left) + preorderTraversal(root.right)


def inorderTraversal(root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    if not root:
        return []
    return inorderTraversal(root.left) + [root.val] + inorderTraversal(root.right)


def lastorderTraversal(root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    if not root:
        return []
    return lastorderTraversal(root.left) + lastorderTraversal(root.right) + [root.val]


def LevelOrder(node):
    if node == None:
        return
    stack = []
    stack.append(node)
    while stack != []:
        node = stack.pop(0)
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
        print(node.val)


if __name__ == "__main__":
    sl = Solution_tree_built()
    a = list('ABDEGHCF')
    b = list('DBGEHACF')
    ansTree = sl.buildTree_pre_in(a, b)
    print(PrintTree(ansTree))
    LevelOrder(ansTree)
