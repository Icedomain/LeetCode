#
# @lc app=leetcode.cn id=189 lang=python3
#
# [189] 旋转数组
#
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        tmp = [0] * len(nums)
        for i in range(len(nums)):
            tmp[(i+k)%len(nums)] = nums[i] #recycle

        for i in range(len(nums)):
            nums[i] = tmp[i]

