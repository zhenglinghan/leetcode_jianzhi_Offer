#!/usr/bin/env python 
# encoding: utf-8 

"""
@version: v1.0
@author: zhenglinghan
@contact: 422807471@qq.com
@software: PyCharm
@file: bitcal_15_hammingWeight.py
@time: 2020/8/12 16:26
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


class Solution(object):
    def hammingWeight1(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        while n:
            res += n & 1
            n >>= 1
        return res

    def hammingWeight2(self, n):
        res = 0
        while n:
            res += 1
            n &= n - 1
        return res

'''
python 中的位运算
位与（&）、位或（|）、位求反（~）、位异或（^）、左移位（<<）和右移位（>>）
1&1 =1 其他都是0
0|0 =0 其他都是1
~101 = 010 对于整数x有~x=-(x+1)
0^0=1^1=0，0^1=1^0=1 相同为1

本题两个思路：
1 尾部和1比较 相同则计数一次，
然后右移位

2 尾部0全变1 （通过原始数字-1完成）
  与原数& 则保留去掉这个1以后之前没有变化的部分
  然后一波去除掉尾部所有的1 继续反复
  n = n&(n-1)
'''

if __name__ == "__main__":
    a = 23
    sl = Solution()
    ans1 = sl.hammingWeight1(a)
    ans2 = sl.hammingWeight2(a)
    print(ans1, ans2)
