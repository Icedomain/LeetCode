#
# @lc app=leetcode.cn id=494 lang=python3
#
# [494] 目标和
#
class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        sums = sum(nums)
        if sums < S or (S + sums)%2 != 0:
            return 0

        target = (S + sums) // 2
        dp = [0]*(target + 1)
        dp[0] = 1
        for num in nums:
            for i in range(target, num-1, -1):
                dp[i] += dp[i - num]
        return dp[-1]

