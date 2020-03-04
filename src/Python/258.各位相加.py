#
# @lc app=leetcode.cn id=258 lang=python3
#
# [258] 各位相加
#
class Solution:
    def addDigits(self, num: int) -> int:
        t = num
        while t >= 10 :
            t = sum([int(char) for char in str(t)])
        return t
        

