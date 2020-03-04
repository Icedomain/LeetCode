#
# @lc app=leetcode.cn id=414 lang=python3
#
# [414] 第三大的数
#
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = list(set(nums))
        if len(nums)<3:
            return max(nums)
        nums.sort()
        return nums[-3]

