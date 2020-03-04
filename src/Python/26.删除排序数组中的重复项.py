#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除排序数组中的重复项
#
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        idx = 0
        while idx < len(nums) -1 :
            if nums[idx] == nums[idx+1]:
                nums.pop(idx)
                idx -= 1
            idx += 1
        return len(nums)
        

