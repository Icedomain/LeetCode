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
        ones,twos = 0,0
        for n in nums:
            # 既不在出现一次的ones，也不在出现两次的twos里面，我们就记录下来，出现了一次，再次出现则会抵消
            ones = (ones ^ n) & ~ twos 
            # 既不在出现两次的twos里面，也不再出现一次的ones里面(不止一次了)，记录出现两次，第三次则会抵消
            twos = (twos ^ n) & ~ ones
        return ones
