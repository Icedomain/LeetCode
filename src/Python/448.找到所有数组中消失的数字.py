#
# @lc app=leetcode.cn id=448 lang=python3
#
# [448] 找到所有数组中消失的数字
#
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        '''
        # time Limit Exceeded
        out = []
        leng = len(nums)
        for i in range(leng):
            if i+1 not in nums:
                out.append(i+1)
        return out
        '''
        for num in nums:
            index = abs(num)-1
            if nums[index]>0:
                nums[index] *= -1
        
        out = []
        for i in range(len(nums)):
            if nums[i]>0:
                out.append(i+1)
        return out



