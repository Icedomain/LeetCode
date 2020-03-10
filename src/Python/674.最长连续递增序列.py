#
# @lc app=leetcode.cn id=674 lang=python3
#
# [674] 最长连续递增序列
#
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        count = 1
        res = 0
        for i in range(len(nums)-1):
            if nums[i] < nums[i+1]:
                count += 1
            else:
                res = max(res,count)
                count = 1
        return max(res,count)


