#
# @lc app=leetcode.cn id=516 lang=python3
#
# [516] 最长回文子序列
#
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[0 ]*n for _ in range(n)]
        # i向前 j往后 
        for i in range(n-1,-1,-1):
            dp[i][i] = 1
            for j in range(i+1 , n ):
                if s[i] == s[j] :
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(
                            dp[i + 1][j], 
                            dp[i][j - 1]
                            )
        return dp[0][-1]


