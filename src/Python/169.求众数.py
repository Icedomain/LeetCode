#
# @lc app=leetcode.cn id=169 lang=python3
#
# [169] 求众数
#
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return sorted(nums)[len(nums)//2]

