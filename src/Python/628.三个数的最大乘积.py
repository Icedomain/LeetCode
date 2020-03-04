#
# @lc app=leetcode.cn id=628 lang=python3
#
# [628] 三个数的最大乘积
#
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        res1 = nums[-1]*nums[-2]*nums[-3]
        res2 = nums[-1]*nums[0]*nums[1]
        return max(res1,res2)

