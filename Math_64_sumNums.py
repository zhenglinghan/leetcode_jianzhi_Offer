#!/usr/bin/env python 
# encoding: utf-8 

"""
@version: v1.0
@author: zhenglinghan
@contact: 422807471@qq.com
@software: PyCharm
@file: Math_64_sumNums.py
@time: 2020/10/8 0:01
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
    def __init__(self):
        self.res = 0

    def sumNums(self, n):
        n > 1 and self.sumNums(n - 1)
        # and 如果前项成立 运行后项， 整个式子赋值由后项决定（后项不成立 赋值=False 成立赋值 true 后项None 则赋值None）
        # and 前项不成立直接返回false 与后项无关
        # 如果是or or 操作如果结果为真，返回第一个结果为真的表达式的值
        # 利用and做短路 跳出递归
        # 整个递归先从输入参数n=1开始 因为不满足前项后项 直接做res+=1 ,return 然后回到上一层n=2，做res+=2……
        self.res += n
        return self.res


if __name__ == "__main__":
    n = 3
    s = Solution()
    print(s.sumNums(n))
