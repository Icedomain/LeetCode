#
# @lc app=leetcode.cn id=224 lang=python3
#
# [224] 基本计算器
#
class Solution:
    def calculate(self, s: str) -> int:
        res = 0
        sign = 1
        stack = []
        i = 0
        while i < len(s):
            c = s[i]
            if c.isdigit():
                start = i
                while i < len(s) and s[i].isdigit():
                    i += 1
                res += sign * int(s[start:i])
                # 因为后加1,不满足while的时候此时的i已经不是数字,需要回退一步,和后边加1对冲
                i -= 1
            elif c == '+':
                sign = 1
            elif c == '-':
                sign = -1
            elif c == "(":
                stack.append(res)
                stack.append(sign)
                res = 0
                sign = 1
            elif c == ")":
                # 现在的res是括号里面的计算结果
                # 需要乘以对应的符号
                res *= stack.pop()
                res += stack.pop()
            i += 1
        return res


