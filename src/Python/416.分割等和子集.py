#
# @lc app=leetcode.cn id=416 lang=python3
#
# [416] 分割等和子集
#
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # 背包问题+动态规划
        target = sum(nums)
        if target % 2 == 1:
            return False
        target //= 2

        # 行nums 列对应 目标值
        dp = [[False]*(target+1) for _ in range(len(nums))]
        # 每一列赋值 
        if nums[0] <= target:
            dp[0][nums[0]] = True

        for i in range(1,len(nums)):
            for j in range(1,target+1):
                if j >= nums[i]:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i]]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[-1][-1]


