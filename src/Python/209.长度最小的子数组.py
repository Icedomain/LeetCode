#
# @lc app=leetcode.cn id=209 lang=python3
#
# [209] 长度最小的子数组
#
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        res = float('inf')
        left = 0
        sumval = 0

        for i in range(len(nums)):
            sumval += nums[i]
            while sumval >= s:
                res = min(res, i-left+1) 
                sumval -= nums[left]
                left += 1

        if res != float('inf'):
            return res
        else:
            return 0
