#
# @lc app=leetcode.cn id=209 lang=python3
#
# [209] 长度最小的子数组
#
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        res = len(nums) + 1
        left = 0
        sumval = 0

        for i in range(len(nums)):
            sumval += nums[i]
            while sumval >= s:
                res = min(res, i-left+1) 
                # 右移动
                sumval -= nums[left]
                left += 1

        if res != len(nums) + 1:
            return res
        else:
            return 0
