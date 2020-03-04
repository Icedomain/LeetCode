#
# @lc app=leetcode.cn id=561 lang=python3
#
# [561] 数组拆分 I
#
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        return sum(nums[::2])

