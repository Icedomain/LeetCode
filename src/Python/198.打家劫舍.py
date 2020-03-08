#
# @lc app=leetcode.cn id=198 lang=python3
#
# [198] 打家劫舍
#
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums :
            return 0
        f1 = 0
        f2 = 0
        for i in nums:
            fi = max(f2+i,f1)
            f1 ,f2 = fi ,f1
        return f1
        

