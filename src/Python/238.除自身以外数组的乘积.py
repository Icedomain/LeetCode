#
# @lc app=leetcode.cn id=238 lang=python3
#
# [238] 除自身以外数组的乘积
#
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]: 
        res = [1] * len(nums)
        right = 1
        for i in range(1, len(nums)):
            res[i] = res[i - 1] * nums[i - 1]
        
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= right
            right *= nums[i]
        return res
