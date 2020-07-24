#
# @lc app=leetcode.cn id=169 lang=python3
#
# [169] 多数元素
#
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        '''
        nums.sort()
        return nums[len(nums)//2]
        '''
        scores = 0
        for n in nums:
            if scores == 0:
                res = n
            if res == n:
                scores += 1
            else:
                scores -= 1
        count = 0
        for n in nums:
            if n == res:
                count += 1
        return res if count >= len(nums)//2 else 0


