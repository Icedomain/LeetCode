#
# @lc app=leetcode.cn id=312 lang=python3
#
# [312] 戳气球
#
class Solution:
    def maxCoins2(self, nums: List[int]) -> int:
        val = [1] + nums + [1]
        return self.solve(val,0, len(val) - 1)

    def solve(self,val,left, right):
        if left >= right - 1:
            return 0
        
        best = 0
        for i in range(left + 1, right):
            total = val[left] * val[i] * val[right]
            total += (
                self.solve(val,left, i) +\
                self.solve(val,i, right) )
            best = max(best, total)
        return best

    def maxCoins(self, nums: List[int]) -> int:
        # 补1
        val = [1] + nums + [1]
        n = len(nums)
        dp = [[0] * (n + 2) for _ in range(n + 2)]

        # i : 0 <- n-1
        # j : i+2 -> n+1
        # k : i+1 -> j-1
        for i in range(n - 1, -1, -1):
            for j in range(i + 2, n + 2):
                for k in range(i + 1, j):
                    total = val[i] * val[k] * val[j]
                    total += dp[i][k] + dp[k][j]
                    dp[i][j] = max(dp[i][j], total)
        
        return dp[0][n + 1]



