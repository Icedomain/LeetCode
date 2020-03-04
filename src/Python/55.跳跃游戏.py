#
# @lc app=leetcode.cn id=55 lang=python3
#
# [55] 跳跃游戏
#
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        start = end = 0
        while start <= end < len(nums) - 1:
            end = max(end, nums[start] + start)
            start += 1
        return end >= len(nums) - 1

