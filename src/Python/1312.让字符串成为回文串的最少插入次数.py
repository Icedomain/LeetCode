#
# @lc app=leetcode.cn id=1312 lang=python3
#
# [1312] 让字符串成为回文串的最少插入次数
#

class Solution:
    def minInsertions(self, s: str) -> int:
        n = len(s)
        dp = [[0]*n for _ in range(n)]

        for i in range(n-2,-1,-1):
            for j in range(i+1,n):
                if s[i] == s[j] :
                    dp[i][j] = dp[i+1][j-1]
                else:
                    dp[i][j] = min(
                        dp[i][j-1],
                        dp[i+1][j],
                    ) + 1
        return dp[0][-1]

