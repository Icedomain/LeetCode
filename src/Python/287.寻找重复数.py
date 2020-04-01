#
# @lc app=leetcode.cn id=287 lang=python3
#
# [287] 寻找重复数
#
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        l,r = 0,len(nums)-1
        while l < r :
            mid = (l+r)//2
            cnt = 0
            for num in nums:
                if num <= mid :
                    cnt += 1

            if cnt > mid :
                r = mid
            else:
                l = mid + 1
        return l
