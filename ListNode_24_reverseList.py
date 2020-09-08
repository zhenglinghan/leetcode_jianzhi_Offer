#!/usr/bin/env python 
# encoding: utf-8 

"""
@version: v1.0
@author: zhenglinghan
@contact: 422807471@qq.com
@software: PyCharm
@file: ListNode_24_reverseList.py
@time: 2020/9/8 23:43
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


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head):
        '''
        最渣渣的单指针，但是需要堆栈做值存储，其实没有改变之前的链表
        :param head:
        :return:
        '''
        stack = []
        if not head:
            return head
        # 把head中的值加入栈里
        while head:
            stack.append(head.val)
            head = head.next
        # 取最后加入的一个，即链表尾作为新的链表头
        cur = ListNode(stack.pop())
        # 记住头部索引
        res = cur
        # 依次给新链表赋值 （链表的前进生成）
        while stack:
            res.next = ListNode(stack.pop())
            res = res.next
        # 返回新链表头部
        return cur

    def reverseList_2(self, head):
        '''
        双指针 pre 和 cur,pre者把pre.next指向cur,每次向前移动
        :param head:
        :return:
        '''
        pre = head
        cur = None
        while pre:
            t = pre.next  # pre的下个位置（pre的原指针）
            pre.next = cur  # 翻转pre的指针
            cur = pre  # cur前移
            pre = t  # pre前移
        return cur

    def reverseList_2(self, head):
        '''
        递归 递归到最后，即为head,返回时当前节点的下一个节点的next指针指向当前节点
        :param head:
        :return:
        '''
        if head==None or head.next ==None:
            return head
        ret = self.reverseList_2(head.next)
        head.next.next = head
        head.next=None
        return ret


if __name__ == "__main__":
    pass
