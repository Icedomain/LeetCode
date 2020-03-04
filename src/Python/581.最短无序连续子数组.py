#
# @lc app=leetcode.cn id=581 lang=python3
#
# [581] 最短无序连续子数组
#
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        num_sort = nums[:] # 浅拷贝和深拷贝
        num_sort.sort()
        n=len(nums)
        i,j=0,n-1
        while i<n and nums[i]==num_sort[i]:
            i += 1
        while j>i+1 and nums[j]==num_sort[j]:
            j -= 1
        return j-i+1


