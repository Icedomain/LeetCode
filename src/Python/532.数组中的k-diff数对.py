#
# @lc app=leetcode.cn id=532 lang=python3
#
# [532] 数组中的K-diff数对
#
from collections import Counter
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        if k < 0 :
            return 0
        # 建字典
        dic = dict(Counter(nums))

        res = 0
        for num in nums:
            # 值在里面 且 k 不为0
            if k != 0 and dic.get(num-k,0) > 0 :
                res += 1
                dic[num-k] = 0
            # k 为0,值有多个
            elif k == 0 and dic.get(num,0) > 1:
                res += 1
                dic[num-k] = 0
        return res

