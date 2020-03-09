#
# @lc app=leetcode.cn id=231 lang=python3
#
# [231] 2的幂
#
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:       
        while n > 1:
            n /= 2
        if n == 1:
            return True
        else:
            return False

