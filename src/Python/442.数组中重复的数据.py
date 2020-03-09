#
# @lc app=leetcode.cn id=442 lang=python3
#
# [442] 数组中重复的数据
#
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        for x in nums:
            x = abs(x)
            # 若x出现过了,x-1对应位置的值是负的(减一是为了超出范围)
            if nums[x-1] < 0:                
                res.append(x)
            else:
                nums[x-1] *= -1
        return res
