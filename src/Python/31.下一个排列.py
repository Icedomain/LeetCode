#
# @lc app=leetcode.cn id=31 lang=python3
#
# [31] 下一个排列
#
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        # 找下一个更大的
        # i为数组倒数第二个值，j为倒数第一个值
        i = len(nums) - 2
        j = len(nums) - 1
        # 从右到左找到第一次断崖
        # 第一次非逆序的地方
        while i >= 0 and nums[i] >= nums[i+1]:
            i -= 1
        
        # 从右到左找到比崖底水平面高的第一个元素
        if i >= 0:
            while j >= 0 and nums[i] >= nums[j]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]

        self.reverse(nums, i+1, len(nums)-1 ) 
    
    # 用于原地反转nums中从start之后的所有元素
    def reverse(self, nums, start, end):
        i, j = start, end
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
        return 
