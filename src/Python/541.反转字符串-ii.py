#
# @lc app=leetcode.cn id=541 lang=python3
#
# [541] 反转字符串 II
#
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        if len(s)<k:
            return s[::-1]
        if len(s)<2*k:
            return s[:k][::-1]+s[k:]
        return s[:k][::-1]+s[k:2*k] + self.reverseStr(s[2*k:],k)

