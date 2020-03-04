#
# @lc app=leetcode.cn id=283 lang=python3
#
# [283] 移动零
#
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ling = []
        for i in range(len(nums)):
            if nums[i] == 0 :
                ling.append(i)
        
        for i in ling[::-1]:
            nums.pop(i)
            nums.append(0)
        return nums
        

