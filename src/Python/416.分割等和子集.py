#
# @lc app=leetcode.cn id=416 lang=python3
#
# [416] 分割等和子集
#
class Solution:
    def canPartition2(self, nums: List[int]) -> bool:
        if not nums: 
            return True
        target = sum(nums)
        if target & 1:
            return False
        target >>= 1
        nums.sort(reverse=True)
        # 有一个大于目标的一半 那就肯定不可能
        if target < nums[0]:
            return False
        return self.dfs(nums, target)

    def dfs(self, nums, total):
        if total == 0:
            return True
        if total < 0:
            return False
        for i in range(len(nums)):
            if self.dfs(nums[:i]+nums[i+1:], total - nums[i]):
                return True
        return False

    def canPartition(self, nums: List[int]) -> bool:
        # 背包问题+动态规划
        target = sum(nums)
        if target % 2 == 1:
            return False
        target >>= 1

        # 行nums 列对应 目标值
        # 从数组的 [0, i] 这个子区间内挑选一些正整数，每个数只能用一次，使得这些数的和恰好等于 j
        dp = [[False]*(target+1) for _ in range(len(nums))]
        # 第一行赋值 用第一个元素能达到多少 
        # 第一列不用赋值 因为和不可能是0
        if nums[0] <= target:
            dp[0][nums[0]] = True

        for i in range(1,len(nums)):
            for j in range(1,target+1):
                # 当前的数可加可不加
                if j >= nums[i]:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i]]
                else:
                    dp[i][j] = dp[i-1][j]
            # 剪枝 提前结束
            if dp[i][target]:
                return True
        return dp[-1][-1]

