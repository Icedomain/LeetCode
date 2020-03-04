#
# @lc app=leetcode.cn id=680 lang=python3
#
# [680] 验证回文字符串 Ⅱ
#
class Solution:
    def validPalindrome(self, s: str) -> bool:
        count = 0
        for i in range(len(s)//2):
            if s[i] != s[-1-i]:
                t, u = s[:i]+s[i+1:], s[:-1-i]+s[len(s)-i:]
                return t == t[::-1] or u == u[::-1]
        return True

        

