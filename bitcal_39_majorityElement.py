#!/usr/bin/env python 
# encoding: utf-8 

"""
@version: v1.0
@author: zhenglinghan
@contact: 422807471@qq.com
@software: PyCharm
@file: bitcal_39_majorityElement.py
@time: 2020/8/12 17:28
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
    '''
    解法1：哈希表统计法： 遍历数组 nums ，用 HashMap 统计各数字的数量，最终超过数组长度一半的数字则为众数。此方法时间和空间复杂度均为 O(N)O(N)
    解法2：数组排序法： 将数组 nums 排序，由于众数的数量超过数组长度一半，因此 数组中点的元素 一定为众数。此方法时间复杂度 O(N log_2 N)O(Nlog2N)
    解法3：* 摩尔投票法核心理念为 “正负抵消” ；时间和空间复杂度分别为 O(N)O(N) 和 O(1)O(1) ；是本题的最佳解法
    解法4:遍历数据统计出现次数,当出现满足条件的就结束，不满足条件就从数据中删除这个数
    '''
    def majorityElement4(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lennums = len(nums)
        numi = None
        countnumi = 0
        while countnumi <= lennums // 2 and nums:
            numi = nums[-1]
            nums_ = list(filter(lambda x: x != numi, nums))
            countnumi = len(nums) - len(nums_)
            nums = nums_
        return numi

    def majorityElement3(self, nums):
        '''
        解法3 摩尔投票法
        从第一个数开始标记1，第二个数如果是相同也为1,不同则为-1
        如果出现抵消，说明我们要找的众数还在后面（后面总票数必然还大于0），所以可以舍弃之前的重新开始找
        :param nums:
        :return:
        '''
        votes = 0
        for num in nums:
            if votes == 0:# 出现抵消就拿当前遍历到的数当做假设众数
                x = num
            votes += (1 if num == x else -1)# 当前假设众数==遍历的数，vote+1 不然vote-1
        # 遍历完必然votes>0 且最后一个假设的x就是众数
        return x

if __name__ == "__main__":
    sl = Solution()
    ans = sl.majorityElement([1, 2, 3, 2, 2, 2, 5, 4, 2])
    print(ans)
