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
        return max(
            self.robb(nums[0:-1]),
            self.robb(nums[len(nums) != 1:])
        )

    def robb(self ,nums):
        now = prev = 0
        for num in nums:
            now , prev = max(now , prev+num) , now
        return now

        

