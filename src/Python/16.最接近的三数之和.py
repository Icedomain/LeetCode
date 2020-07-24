#
# @lc app=leetcode.cn id=16 lang=python3
#
# [16] 最接近的三数之和
#
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = sum(nums[0:3])

        for i in range(len(nums)-2):
            l,r = i+1,len(nums)-1
            while l < r:
                sum_val = nums[i]+nums[l]+nums[r]
                if abs(res-target)>abs(sum_val-target):
                    res = sum_val
                if sum_val < target:
                    l+=1
                else:
                    r -= 1
        return res

