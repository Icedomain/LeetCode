#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子序和
#
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        temp = maxsum = nums[0]
        for num in nums[1:]:
            # num 要么单独一个子列,要么归入别的子列
            temp = max(num,temp+num)
            maxsum = max(temp,maxsum)
        return maxsum

