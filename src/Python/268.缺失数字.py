#
# @lc app=leetcode.cn id=268 lang=python3
#
# [268] 缺失数字
#
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return  len(nums)*(len(nums)+1)//2 - sum(nums)

