#
# @lc app=leetcode.cn id=66 lang=python3
#
# [66] 加一
#
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        '''
        # 数值操作
        num = 0
        for i in range(len(digits)):
            num = num * 10 + digits[i]
        num = num + 1
        res = []
        while num > 0:
            res.append(num%10)
            num //= 10
        res.reverse()
        return res
        '''

        # 列表操作
        digits[-1] += 1
        digits.insert(0, 0)
        for i in range(len(digits)-1,0,-1):
            carry = digits[i] // 10
            digits[i] %= 10
            digits[i-1] += carry

        if digits[0] == 0:
            digits.pop(0)
        return digits

