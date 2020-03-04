#
# @lc app=leetcode.cn id=152 lang=python3
#
# [152] 乘积最大子序列
#
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if nums is None:
            return 0
        maxtmp = mintmp = maxval = nums[0]
        for i in range(1,len(nums)):
            mx ,mn = maxtmp ,mintmp
            maxtmp = max(nums[i] , nums[i]*mx ,nums[i]*mn)
            mintmp = min(nums[i] , nums[i]*mx ,nums[i]*mn)
            maxval = max(maxtmp,maxval)
        return maxval


        

