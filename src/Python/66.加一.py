#
# @lc app=leetcode.cn id=66 lang=python3
#
# [66] 加一
#
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = 0
        for i in range(len(digits)):
            num += digits[i] * pow(10, len(digits) - i -1 )
        num = num + 1
        out = []
        while num > 0:
            out.append(num%10)
            num //= 10
        out.reverse()
        return out
        

