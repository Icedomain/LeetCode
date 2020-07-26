#
# @lc app=leetcode.cn id=191 lang=python3
#
# [191] 位1的个数
#
class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            count += n & 1
            n >>= 1
        return count

