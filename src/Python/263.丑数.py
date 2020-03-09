#
# @lc app=leetcode.cn id=263 lang=python3
#
# [263] 丑数
#
class Solution:
    def isUgly(self, num: int) -> bool:
        if num <= 0 :
            return False

        divisors = [2, 3, 5]
        for d in divisors:
            while num % d == 0:
                num /= d
        return num == 1


