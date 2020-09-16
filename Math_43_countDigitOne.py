#!/usr/bin/env python 
# encoding: utf-8 

"""
@version: v1.0
@author: zhenglinghan
@contact: 422807471@qq.com
@software: PyCharm
@file: Math_43_countDigitOne.py
@time: 2020/9/16 0:09
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
    '''
    总体求法：
    1~n所有树个位，10位，100位上1的个数相加即可

    例子 2304
    digit=10 当前位10


    求0~2304中10位上1出现次数
    curr = 0 则10位出现次数只看高位 23*n （0~100中10位为1的次数 0~100 中有10个10~19 ）所以 n是10=digit
    公式：high*digit

    求0~2314中10位上1出现次数
    curr = 1 则10位出现次数只看高位 23*n （0~100中10位为1的次数 0~100 中有10个10~19 ）所以 n是10=digit
    还有本身curr =1 2310 所以+1
    还有low个本身：2311 2312 2313 2314 所以low*1
    公式：high*digit+low+1

    求0~2324中10位上1出现次数
    curr > 1 则10位出现次数只看高位 23*n （0~100中10位为1的次数 0~100 中有10个10~19 ）所以 n是10
    还有本身2310~2319 10个  =digit
    公式：high*digit+digit

    然后求百位digit=100
    '''

    def countDigitOne(self, n):
        digit, res = 1, 0  # 位，结果
        high, cur, low = n // 10, n % 10, 0  # 高位， 当前位 ， 低位可以组成n high*10*10^0+cur*10^0+low*10^0
        while high != 0 or cur != 0:
            if cur == 0:
                res += high * digit
            elif cur == 1:
                res += high * digit + low + 1
            else:
                res += (high + 1) * digit
            low += cur * digit  # 将 cur 加入 low ，组成下轮 low
            cur = high % 10  # 下轮 cur 是本轮 high 的最低位
            high //= 10  # 将本轮 high 最低位删除，得到下轮 high
            digit *= 10  # 位因子每轮 × 10
        return res

    def countDigitOne_self(self, n):
        digit, res = 1, 0  # digit从10^0开始
        high, curr, low = n // 10, n % 10, 0  # 个位
        while high != 0 or curr != 0:  # 如果high!=0,则没有累加完毕，如果curr!=0至少个位不等于0可以开始
            if curr == 0:
                res += high * digit
            elif curr == 1:
                res += high * digit + low + 1
            else:
                res += high * digit + digit
            # 个位看完看10位，将个位放入low
            # 10位看完看100位，low=10位*10+个位
            low += curr * digit
            curr = high % 10
            high = high // 10
            digit = digit * 10
        return res


if __name__ == "__main__":
    '''
    总体规律
    now = 1
    for i in [10,100,1000,10000,100000]:   
        dig = np.log10(i)
        if i>10:
            now = now*10+10**(dig-1)
        print(i,now)
    要判断位数是否等于1
    '''
    n = 100
    s = Solution()
    ans = s.countDigitOne_self(n)
    print(ans)
