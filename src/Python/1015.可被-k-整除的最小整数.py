#
# @lc app=leetcode.cn id=1015 lang=python3
#
# [1015] 可被 K 整除的最小整数
#
class Solution:
    def smallestRepunitDivByK(self, K: int) -> int:
        if K%2 == 0 or K%5 == 0:
            return -1
        temp = 1
        len = 1
        while temp % K :
            temp = (temp % K) * 10 + 1
            len += 1
        return len
