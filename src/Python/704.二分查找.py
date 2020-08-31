#
# @lc app=leetcode.cn id=704 lang=python3
#
# [704] 二分查找
#

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums or target < nums[0] or target > nums[-1]:
            return -1
        l,r = 0 , len(nums) - 1
        while l <= r:
            mid = (l+r)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return -1


