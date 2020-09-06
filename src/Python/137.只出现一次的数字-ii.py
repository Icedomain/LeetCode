#
# @lc app=leetcode.cn id=137 lang=python3
#
# [137] 只出现一次的数字 II
#
class Solution:
    def singleNumber2(self, nums: List[int]) -> int:
        return (3 * sum(set(nums)) - sum(nums) ) //2 

    def singleNumber(self, nums: List[int]) -> int:
        # 出现一次的位，和两次的位
        b1,b2 = 0,0
        for n in nums:
            # 既不在出现一次的b1，也不在出现两次的b2里面，我们就记录下来，出现了一次，再次出现则会抵消
            b1 = (b1 ^ n) & ~ b2 
            # 既不在出现两次的b2里面，也不再出现一次的b1里面(不止一次了)，记录出现两次，第三次则会抵消
            b2 = (b2 ^ n) & ~ b1
        return b1
