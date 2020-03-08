#
# @lc app=leetcode.cn id=167 lang=python3
#
# [167] 两数之和 II - 输入有序数组
#
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0 
        r = len(numbers)-1
        while l <= r:
            temp = numbers[l]+numbers[r]
            if temp == target:
                return [l+1 , r+1]
            elif temp < target :
                l += 1
            elif temp > target:
                r -= 1


