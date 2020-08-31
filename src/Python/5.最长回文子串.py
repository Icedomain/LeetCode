#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s :
            return ''
        
        # 动态规划
        dp = [[False for _ in range(len(s))] for _ in range(len(s))]
        left, right, max_len = 0, 0, 0
        
        for j in range(len(s)):
            # 对角线置1
            dp[j][j] = True
            for i in range(j-1,-1,-1):
                if s[i] == s[j] and (j-i < 2 or dp[i+1][j-1]):
                    dp[i][j] = True
                if dp[i][j] and max_len < j-i+1:
                    max_len = j - i + 1
                    left, right = i, j
        return s[left:right+1]

