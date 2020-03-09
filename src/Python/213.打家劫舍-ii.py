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
        mx = prev = 0
        for i in nums:
            temp = mx
            mx = max(mx , prev + i )
            prev = temp
        return mx

