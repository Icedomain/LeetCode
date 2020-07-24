#
# @lc app=leetcode.cn id=343 lang=python3
#
# [343] 整数拆分
#
import math
class Solution:
    def integerBreak(self, n: int) -> int:
        '''
        dp = [1]*(n+1)
        # dp[0] = 0
        # dp[1] = 1
        # dp[2] = 1
        for i in range(2,n+1):
            for j in range(1,i//2+1):
                dp[i] = max(dp[i],
                            max(j,dp[j])*max(i-j,dp[i-j])
                            )
        return dp[-1]
        '''

        if n <= 3: 
            return n - 1
        # 尽可能的多3的段
        a, b = n // 3, n % 3
        if b == 0: 
            # 全3的段
            return int(math.pow(3, a))
        elif b == 1: 
            # 3段 + 2 段+ 2段 (2*2>3*1)
            return int(math.pow(3, a - 1) * 4)
        else:
            # 3 段 2 段
            return int(math.pow(3, a) * 2)

