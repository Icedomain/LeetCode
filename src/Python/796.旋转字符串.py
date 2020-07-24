#
# @lc app=leetcode.cn id=796 lang=python3
#
# [796] 旋转字符串
#
class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        return (A in B*2) and (len(A) == len(B))

