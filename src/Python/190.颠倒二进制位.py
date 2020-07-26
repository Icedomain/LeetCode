#
# @lc app=leetcode.cn id=190 lang=python3
#
# [190] 颠倒二进制位
#
class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        bitsSize = 31
        while bitsSize >= 0 and n :
            res += ((n & 1) << bitsSize)
            n >>= 1
            bitsSize -= 1
        return res
