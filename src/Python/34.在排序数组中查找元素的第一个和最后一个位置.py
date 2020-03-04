#
# @lc app=leetcode.cn id=34 lang=python3
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]
        min = 0
        max = len(nums) - 1
        while min <= max:
            pos = (min + max) // 2
            if nums[pos] > target:
                max = pos - 1
            elif nums[pos] < target:
                min = pos + 1
            else:
                # when nums[pos] == target
                # find the min and max
                for i in range(pos, max + 1) :
                    if nums[i] == target:
                        max = i
                for i in range(pos, min -1 , -1) :
                    if nums[i] == target:
                        min = i
                return [min, max]
        return [-1, -1]

