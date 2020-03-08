#
# @lc app=leetcode.cn id=169 lang=python3
#
# [169] 多数元素
#
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums)//2]
