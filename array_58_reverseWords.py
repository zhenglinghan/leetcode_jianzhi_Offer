#!/usr/bin/env python 
# encoding: utf-8 

"""
@version: v1.0
@author: zhenglinghan
@contact: 422807471@qq.com
@software: PyCharm
@file: array_58_reverseWords.py
@time: 2020/10/5 0:33
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


class Solution:
    # 单指针 占用内存多
    def reverseWords1(self, s):
        s = s.strip()
        s = list(s)
        res = []
        word = ''
        while s:
            w = s.pop(0)
            if w != ' ':
                word += w
            else:
                if len(word) > 0:
                    res.append(word)
                    word = ''
        res.append(word)
        return ' '.join(res[::-1])

    # 双指针直接切片
    # 常用语提取单子，片段
    def reverseWords2(self, s):
        s = s.strip()  # 删除首尾空格
        i = j = len(s) - 1  # 都从尾部开始遍历
        res = []
        while i >= 0:
            while i >= 0 and s[i] != ' ':
                i -= 1  # 搜索首个空格 j作为切片单词的末尾不动 i向前搜索
            res.append(s[i + 1: j + 1])  # 添加单词 遇到空格就添加
            # 可能遭遇多个空格 全部跳过
            while s[i] == ' ':
                i -= 1  # 跳过单词间空格
            j = i  # j 指向下个单词的尾字符 交换i，j j作为新的单次末尾 原本i落到新的单词尾部
        return ' '.join(res)  # 拼接并返回

    # 语法糖
    def reverseWords3(self, s):
        return ' '.join(s.strip().split()[::-1])


if __name__ == "__main__":
    pass
