#
# @lc app=leetcode.cn id=153 lang=python3
#
# [153] 寻找旋转排序数组中的最小值
#
class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1 or nums[0] < nums[-1]: # 升序
            return nums[0]
        l , r = 0, len(nums)-1
        while l < r :
            mid = (l+r)//2
            # 左边
            if nums[0] <= nums[mid]:
                l = mid + 1
            # 在右边
            else:
                r = mid
        return nums[l]

