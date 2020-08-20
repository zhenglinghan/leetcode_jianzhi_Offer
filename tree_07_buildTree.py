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


def postorderTraversal(root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    if not root:
        return []
    return postorderTraversal(root.left) + postorderTraversal(root.right) + [root.val]


# 3种非递归遍历树的方式
# 需要用到两个栈

def bin_tree_pre_order_traverse1(root):
    '''
    利用两个栈实现
    '''
    s1 = []
    s2 = []
    s1.append(root)
    while s1:
        node = s1.pop()
        s2.append(node)
        if node.left:
            s1.append(node.left)
        if node.right:
            s1.append(node.right)
    while s2:
        print(s2.pop().value)


def bin_tree_in_order_traverse1(root):
    '''
    利用两个栈实现
    '''
    s1 = []
    s2 = []
    s1.append(root)
    while s1:
        node = s1.pop()
        s2.append(node)
        if node.left:
            s1.append(node.left)
        if node.right:
            s1.append(node.right)
    while s2:
        print(s2.pop().value)


def bin_tree_post_order_traverse1(root):
    '''
    利用两个栈实现
    '''
    s1 = []
    s2 = []
    s1.append(root)
    while s1:
        node = s1.pop()
        s2.append(node)
        if node.left:
            s1.append(node.left)
        if node.right:
            s1.append(node.right)
    while s2:
        print(s2.pop().value)


class Solution(object):
    def buildTree(self, preorder, inorder, postorder):
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
        # 因为后续pop（0）以后中（pop(0)） 前 后，最外侧是前，所以下方应该先求左子树
        indexroot = inorder.index(root.val)  # 这个跟的子树的访问顺序里中序为左 + 根 +右，找到根的位置
        # 对剩下的节点进行递归
        root.left = self.buildTree_pre_in(preorder, inorder[:indexroot])  # 对于根的左边子树仍然做一个根据前序，中序 重建的过程
        root.right = self.buildTree_pre_in(preorder, inorder[indexroot + 1:])  # 对于根的右边子树仍然做一个根据前序，中序 重建的过程
        return root  # 返回根节点代表这颗子树

    def buildTree_pre_post(self, preorder, postorder):
        """
        前序 后序恢复整颗树
        :param preorder:
        :param postorder:
        :return:
        """
        # 无解
        pass

    def buildTree_in_post(self, inorder, postorder):
        """
        中序 后序恢复整颗树
        :param inorder:
        :param postorder:
        :return:
        """
        if not inorder or not postorder:
            return None
        '''
        前序  根 左 右
        中序  左 根 右
        后序  左 右 根
        '''
        # postorder中弹出根节点 在中序中找到 找到在中序中的索引
        root = TreeNode(postorder.pop())
        # 因为后续pop以后前 后 中（pop），最外侧是后，所以下方应该先求右子树
        index = inorder.index(root.val)
        #   # 这里是先求右子树！
        root.right = self.buildTree_in_post(inorder[index + 1:], postorder)
        root.left = self.buildTree_in_post(inorder[:index], postorder)
        return root  # 返回根节点代表这颗子树


'''
BFS 三种打印
'''


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


def PrintTree_null(pRoot):
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
            if out_node:
                temp.append(out_node.val)
            else:
                temp.append('Null')
            if out_node:
                stack.append(out_node.left)
                stack.append(out_node.right)
        output.append(temp)
    return output


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
    c = list('DGHEBFCA')
    ansTree = sl.buildTree_pre_in(a, b)
    print(PrintTree(ansTree))
    print(PrintTree_null(ansTree))
    print(postorderTraversal(ansTree))
    ansTree = sl.buildTree_in_post(b, c)
    print(postorderTraversal(ansTree))
    # print(PrintTree(ansTree))
    # LevelOrder(ansTree)
