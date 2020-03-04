#
# @lc app=leetcode.cn id=485 lang=python3
#
# [485] 最大连续1的个数
#
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxval = 0
        tmp = 0
        for i in range(len(nums)):
            if nums[i] != 0 :
                tmp += 1
            else:
                maxval = max(maxval,tmp)
                tmp = 0
        maxval = max(maxval,tmp)
        return maxval 

