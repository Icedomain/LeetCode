#
# @lc app=leetcode.cn id=7 lang=python3
#
# [7] 整数反转
#
class Solution:
    def reverse(self, x: int) -> int:
        sign = 1 if x > 0 else -1
        res = 0
        x = abs(x)
        while x :
            res = res*10 + x%10
            if res > 2**31 - 1:
                return 0
            x = x//10

        return sign * res

