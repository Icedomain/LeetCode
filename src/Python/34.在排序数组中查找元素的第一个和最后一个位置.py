#
# @lc app=leetcode.cn id=34 lang=python3
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                # when nums[mid] == target
                # find the l and r
                for i in range(mid, r + 1) :
                    if nums[i] == target:
                        r = i
                for i in range(mid, l -1 , -1) :
                    if nums[i] == target:
                        l = i
                return [l, r]
        return [-1, -1]

