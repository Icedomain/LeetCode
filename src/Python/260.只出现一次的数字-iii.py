#
# @lc app=leetcode.cn id=260 lang=python3
#
# [260] 只出现一次的数字 III
#
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        # 异或的结果
        diff = 0
        # 得到 x^y
        for num in nums:
            diff ^= num
        # 区分x和y, 得到x和y不同的某一位
        ret = 1
        while ret & diff == 0:
            ret <<= 1
        res = [0, 0]
        for num in nums:
            # 除了x外，其他&=0的数成对出现
            if num & ret:
                res[0] ^= num
            # 除了y外，其他&=1的数成对出现
            else:
                res[1] ^= num
        return res
