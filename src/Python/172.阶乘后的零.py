#
# @lc app=leetcode.cn id=172 lang=python3
#
# [172] 阶乘后的零
#
class Solution:
    def trailingZeroes(self, n: int) -> int:
        count = 0
        while n >0:
            n //= 5
            count += n
        return count
