#
# @lc app=leetcode.cn id=41 lang=python3
#
# [41] 缺失的第一个正数
#
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        self.bucket_sort(nums)

        for i in range(len(nums)):
            if nums[i] != (i+1):
                return i+1
        return len(nums)+1

    def bucket_sort(self,nums):
        for i in range(len(nums)):
            while 0 <= nums[i] < len(nums) and nums[i] != nums[nums[i]-1]:
                temp = nums[i]-1
                nums[i] = nums[temp]
                nums[temp] = temp +1 
        return

