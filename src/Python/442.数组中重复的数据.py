#
# @lc app=leetcode.cn id=442 lang=python3
#
# [442] 数组中重复的数据
#
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        returnlist=[]
        for x in nums:
            x = abs(x)
            if nums[x-1]<0:# 出现过了
                returnlist.append(x)
            else:
                nums[x-1]*=-1
        return returnlist


