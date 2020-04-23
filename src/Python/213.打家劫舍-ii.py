#
# @lc app=leetcode.cn id=213 lang=python3
#
# [213] 打家劫舍 II
#
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        # 奇偶串
        return max(
            self.robb(nums[0:-1]),
            self.robb(nums[1:])
        )

    def robb(self ,nums):
        f1 = 0
        f2 = 0
        for i in nums:
            fi = max(f2+i,f1)
            f1 ,f2 = fi ,f1
        return f1
