#!/usr/bin/env python 
# encoding: utf-8 

"""
@version: v1.0
@author: zhenglinghan
@contact: 422807471@qq.com
@software: PyCharm
@file: ListNode_35_copyRandomList.py
@time: 2020/9/10 23:01
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
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    '''
    用户复制的哈希表
    key是原node value是copy后的node,通过random去向各个原node,并取出copy后的node
    '''
    def copyRandomList_0(self, head):
        '''
        dfs 认为是在图上进行dfs遍历 维护一张哈希表，访问过的节点直接返回并进行复制
        算法：深度优先搜索
        从头结点 head 开始拷贝；
        由于一个结点可能被多个指针指到，因此如果该结点已被拷贝，则不需要重复拷贝；
        如果还没拷贝该结点，则创建一个新的结点进行拷贝，并将拷贝过的结点保存在哈希表中；
        使用递归拷贝所有的 next 结点，再递归拷贝所有的 random 结点。

        :param head:
        :return:
        '''

        def dfs(head):
            if not head:
                return None
            if head in visited:
                return visited[head]
            # 创建新结点
            copy = Node(head.val, None, None)
            visited[head] = copy
            copy.next = dfs(head.next)  # copy.next就是head.next的所有 先走完next
            copy.random = dfs(head.random)  # copy.random就是head.random的所有 再从最后一个节点的random开始放入hash表
            return copy

        visited = {}
        return dfs(head)

    def copyRandomList_1(self, head):
        '''
        算法：广度优先搜索
        创建哈希表保存已拷贝结点，格式 {原结点：拷贝结点}
        创建队列，并将头结点入队；
        当队列不为空时，弹出一个结点，如果该结点的 next 结点未被拷贝过，则拷贝 next 结点并加入队列；同理，如果该结点的 random 结点未被拷贝过，则拷贝 random 结点并加入队列；

        :param head:
        :return:
        '''
        visited = {}

        def bfs(head):
            if not head:
                return head
            clone = Node(head.val, None, None)  # 创建新结点
            queue = []
            queue.append(head)
            visited[head] = clone
            while queue:
                # 还没复制过的下方节点
                tmp = queue.pop()
                # 类似二叉树，左子树，右子树
                # queue入栈 tmp的next 与 random 但是前提是tmp有next,random
                # 所以分别判断，并复制放入hash set
                if tmp.next and tmp.next not in visited:
                    visited[tmp.next] = Node(tmp.next.val, [], [])
                    queue.append(tmp.next)
                if tmp.random and tmp.random not in visited:
                    visited[tmp.random] = Node(tmp.random.val, [], [])
                    queue.append(tmp.random)
                # 直接当层完成复制
                visited[tmp].next = visited.get(tmp.next)
                visited[tmp].random = visited.get(tmp.random)
            return clone

        return bfs(head)

    def copyRandomList_2(self, head):
        '''
        该方法的思路比较直接，对于一个结点，分别拷贝此结点、next 指针指向的结点、random 指针指向的结点， 然后进行下一个结点...
        如果遇到已经出现的结点，那么我们不用拷贝该结点，只需将 next 或 random 指针指向该结点即可。
        :param head:
        :return:
        '''
        visited = {}

        def getClonedNode(node):
            if node:
                if node in visited:
                    return visited[node]
                else:
                    visited[node] = Node(node.val, None, None)
                    return visited[node]
            return None

        if not head: return head
        old_node = head
        new_node = Node(old_node.val, None, None)
        visited[old_node] = new_node

        while old_node:
            new_node.random = getClonedNode(old_node.random)
            new_node.next = getClonedNode(old_node.next)

            old_node = old_node.next
            new_node = new_node.next
        return visited[head]

    def copyRandomList_3(self, head):
        '''
        我们也可以不使用哈希表的额外空间来保存已经拷贝过的结点，
        而是将链表进行拓展，在每个链表结点的旁边拷贝，比如 A->B->C 变成 A->A'->B->B'->C->C'，
        然后将拷贝的结点分离出来变成 A->B->C和A'->B'->C'，最后返回 A'->B'->C'。
        :param head:
        :return:
        '''
        if not head: return head
        cur = head
        while cur:
            new_node = Node(cur.val, None, None)  # 克隆新结点
            new_node.next = cur.next
            cur.next = new_node  # 克隆新结点在cur 后面
            cur = new_node.next  # 移动到下一个要克隆的点
        cur = head

        while cur:  # 链接random
            cur.next.random = cur.random.next if cur.random else None
            cur = cur.next.next

        cur_old_list = head  # 将两个链表分开
        cur_new_list = head.next
        new_head = head.next
        while cur_old_list:
            cur_old_list.next = cur_old_list.next.next
            cur_new_list.next = cur_new_list.next.next if cur_new_list.next else None
            cur_old_list = cur_old_list.next
            cur_new_list = cur_new_list.next
        return new_head


if __name__ == "__main__":
    a = Node(1, None, None)
    b = Node(2, None, None)
    c = Node(3, None, None)
    d = Node(4, None, None)
    e = Node(5, None, None)
    f = Node(6, None, None)
    a.next = b
    a.random = e
    b.next = c
    b.random = f
    c.next = d
    c.random = a
    d.next = e
    d.random = f
    e.next = f
    e.random = None
    f.next = None
    f.random = d
    s = Solution()
    ans = s.copyRandomList_1(a)
