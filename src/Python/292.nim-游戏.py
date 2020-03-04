#
# @lc app=leetcode.cn id=292 lang=python3
#
# [292] Nim 游戏
#
class Solution:
    def canWinNim(self, n: int) -> bool:
        return n%4 != 0

