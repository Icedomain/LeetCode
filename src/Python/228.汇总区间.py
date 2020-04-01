#
# @lc app=leetcode.cn id=228 lang=python3
#
# [228] 汇总区间
#
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        res = []
        i = 0 
        while i < len(nums):
            j = i
            while  j+1<len(nums) and (nums[j + 1] - nums[j] <= 1):
                j += 1
            
            if i == j:
                res.append( str(nums[i]) )
            else:
                res.append( str(nums[i]) + "->" + str(nums[j]) )
            i = j+1
        return res
