#
# @lc app=leetcode.cn id=152 lang=python3
#
# [152] 乘积最大子序列
#
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        maxtmp = mintmp = res = nums[0]
        for i in range(1,len(nums)):
            maxtmp ,mintmp =max(nums[i] , nums[i]*maxtmp ,nums[i]*mintmp) ,\
                            min(nums[i] , nums[i]*maxtmp ,nums[i]*mintmp)
            res = max(maxtmp,res)
        return res

