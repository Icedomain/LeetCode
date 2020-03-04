#
# @lc app=leetcode.cn id=33 lang=python3
#
# [33] 搜索旋转排序数组
#
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        l,r = 0 , len(nums) -1 

        while l <= r:
            mid = (l+r)//2
            if nums[mid] == target:
                return mid
            # mid在前半段 或者l mid r 都在右边
            if nums[l] <= nums[mid]: 
                if nums[l] <= target <= nums[mid]:
                    r = mid -1
                else:
                    l = mid +1
            # l 在左半段 、mid 在后半段
            else: 
                if nums[mid] <= target <= nums[r]:
                    l = mid +1
                else:
                    r = mid -1
        return -1
        

