#
# @lc app=leetcode.cn id=643 lang=python3
#
# [643] 子数组最大平均数 I
#
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        tmp = maxmean = sum(nums[:k])
        for i in range(k,len(nums)):
            tmp += (nums[i]-nums[i-k])
            maxmean = max(maxmean,tmp)
        return maxmean/k

