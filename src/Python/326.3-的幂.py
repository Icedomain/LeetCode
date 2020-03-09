#
# @lc app=leetcode.cn id=326 lang=python3
#
# [326] 3的幂
#
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        while n > 1:
            n /= 3
        if n == 1:
            return True
        else:
            return False
