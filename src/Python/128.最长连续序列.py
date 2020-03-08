#
# @lc app=leetcode.cn id=128 lang=python3
#
# [128] 最长连续序列
#
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxLen = 0
        while nums:
            n = nums.pop()
            # 往大处搜索
            i1 = n + 1
            while i1 in nums:
                nums.remove(i1)
                i1 += 1
            # 往小处搜索
            i2 = n - 1
            while i2 in nums:
                nums.remove(i2)
                i2 -= 1
            maxLen = max(maxLen, i1 - i2 - 1)
        return maxLen


