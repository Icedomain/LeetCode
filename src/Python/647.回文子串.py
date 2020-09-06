#
# @lc app=leetcode.cn id=647 lang=python3
#
# [647] 回文子串
#
class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        res = 0
        for i in range(n):
            dp[i][i] = 1
            for j in range(i+1):
                if s[i] == s[j] and (i - j < 2 or dp[j + 1][i - 1]):
                    dp[j][i] = 1
                    res += 1
        return res





