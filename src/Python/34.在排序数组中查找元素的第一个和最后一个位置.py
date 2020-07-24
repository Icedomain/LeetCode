#
# @lc app=leetcode.cn id=34 lang=python3
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]
        l , r = 0 , len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                # when nums[mid] == target
                lc = rc = mid 
                while lc >= 0 and nums[lc] == target:
                    lc -= 1
                while rc <= len(nums)-1 and nums[rc] == target:
                    rc += 1
                return [lc+1, rc-1]
        return [-1, -1]

