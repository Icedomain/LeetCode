#
# @lc app=leetcode.cn id=217 lang=python3
#
# [217] 存在重复元素
#
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))

