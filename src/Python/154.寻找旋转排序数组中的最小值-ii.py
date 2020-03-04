#
# @lc app=leetcode.cn id=154 lang=python3
#
# [154] 寻找旋转排序数组中的最小值 II
#

class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1 or nums[0] < nums[-1]: # 升序
            return nums[0]
        
        l , r = 0, len(nums)-1
        while l < r :
            mid = (l+r)//2
            # 左边
            if nums[mid] > nums[r]: 
                l = mid + 1
            # 在右边            
            elif nums[mid] < nums[r]: 
                r = mid
            # nums[mid] == nums[r]情况
            else: 
                r -= 1
        return nums[l]
