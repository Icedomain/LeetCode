#
# @lc app=leetcode.cn id=283 lang=python3
#
# [283] 移动零
#
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        '''
        zeros = []
        for i in range(len(nums)):
            if nums[i] == 0 :
                zeros.append(i)
        
        for i in zeros[::-1]:
            nums.pop(i)
            nums.append(0)
        return nums
        '''
        j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[j] = nums[i]
                j += 1
        for i in range(j,len(nums)):
            nums[i] = 0

