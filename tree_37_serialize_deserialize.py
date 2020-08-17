#!/usr/bin/env python 
# encoding: utf-8 

"""
@version: v1.0
@author: zhenglinghan
@contact: 422807471@qq.com
@software: PyCharm
@file: tree_37_serialize_deserialize.py
@time: 2020/8/17 22:52
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


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


'''
反序列化 deserialize ：
基于本文一开始分析的 “ node , node.left , node.right ” 在序列化列表中的位置关系，可实现反序列化。

利用队列按层构建二叉树，借助一个指针 i 指向节点 node 的左、右子节点，每构建一个 node 的左、右子节点，指针 i 就向右移动 1 位。

算法流程：
特例处理： 若 data 为空，直接返回 null ；
初始化： 序列化列表 vals （先去掉首尾中括号，再用逗号隔开），指针 i = 1i=1 ，根节点 root（值为 vals[0] ），队列 queue（包含 root ）；
按层构建： 当 queue 为空时跳出；
节点出队，记为 node ；
构建 node 的左子节点：node.leftnode.left 的值为 vals[i] ，并将 node.left 入队；
执行 i+=1 ；
构建 node 的右子节点：node.leftnode.left 的值为 vals[i] ，并将 node.left 入队；
执行 i+=1 ；
返回值： 返回根节点 rootroot 即可。
复杂度分析：
时间复杂度 O(N) ： NN 为二叉树的节点数，按层构建二叉树需要遍历整个 vals ，其长度最大为 2N+12N+1 。
空间复杂度 O(N) ： 最差情况下，队列 queue 同时存储 \frac{N + 1}{2} 
2N+1 个节点，因此使用 O(N)O(N) 额外空间。

'''


class Codec:

    def serialize(self, root):
        if not root: return "[]"
        queue = []
        queue.append(root)
        res = []
        while queue:
            node = queue.pop(0)  # 队首先进先出
            if node:
                res.append(str(node.val))
                queue.append(node.left)  # 不用判断是否为空，直接加入因为后续要保留null位置
                queue.append(node.right)
            else:
                res.append("null")
        return '[' + ','.join(res) + ']'

    def deserialize(self, data):
        if data == "[]":
            return
        vals, i = data[1:-1].split(','), 1# 指针位i = 1
        root = TreeNode(int(vals[0]))# 初始化根
        queue = []
        queue.append(root)# 下一层的根节点遍历生长！ 长出对应的值可能是node.val 可能是null
        while queue:
            node = queue.pop(0)
            if vals[i] != "null":
                node.left = TreeNode(int(vals[i]))
                queue.append(node.left)
            i += 1# 长过一个就+1 如果是null 就不长 也要加1
            if vals[i] != "null":
                node.right = TreeNode(int(vals[i]))
                queue.append(node.right)
            i += 1
        return root


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(5)
    codec = Codec()
    ans1 = codec.serialize(root)
    ans2 = codec.serialize(root)
