#
# @lc app=leetcode.cn id=415 lang=python3
#
# [415] 字符串相加
#
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        res = []
        i, j = len(num1) - 1, len(num2) - 1
        carry = 0
        while i >= 0 or j >= 0:
            n1 = int(num1[i]) if i >= 0 else 0
            n2 = int(num2[j]) if j >= 0 else 0
            tmp = n1 + n2 + carry
            carry = tmp // 10
            res.append(str(tmp % 10))
            i -= 1
            j -= 1
        if carry :
            res.append(str(carry) )
        
        return "".join(reversed(res))


