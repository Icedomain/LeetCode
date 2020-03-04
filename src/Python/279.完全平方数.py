#
# @lc app=leetcode.cn id=279 lang=python3
#
# [279] 完全平方数
#
class Solution:
    _dp = [0]
    def numSquares(self, n: int) -> int:
        '''
        # 性能测试过不了
        # 先扣出来2的部分
        while n % 4 == 0 :
            n /= 4
        if n %8 == 7:
            return 4
        n = int(n)
        dp = [0]+[float('inf') for i in range(n)]
        # 对每个数来说
        for i in range(n + 1):
            j = 1
            while i >= j**2 :
                # 取小
                dp[i] = min(dp[i], dp[i- j**2] + 1)
                j += 1
                
        return dp[n]
        '''
        dp = self._dp
        while len(dp) <= n:
            dp += min(dp[-i*i] for i in range(1, int(len(dp)**0.5+1))) + 1,
        return dp[n]



        

