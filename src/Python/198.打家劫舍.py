#
# @lc app=leetcode.cn id=198 lang=python3
#
# [198] 打家劫舍
#
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums :
            return 0
        f_1 = 0
        f_2 = 0
        for i in nums:
            f_i = max(f_2+i,f_1)
            f_1 ,f_2 = f_i ,f_1
        return f_1
        

