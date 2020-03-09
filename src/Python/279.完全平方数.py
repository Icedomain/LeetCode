#
# @lc app=leetcode.cn id=279 lang=python3
#
# [279] 完全平方数
#
class Solution:
    def numSquares(self, n: int) -> int:
        dp = list(range(n+1))
        for i in range(2,n+1):
            for j in range(1,int(i**(0.5))+1):
                dp[i]=min(dp[i],dp[i-j*j]+1)
        return dp[-1]


