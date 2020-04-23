#
# @lc app=leetcode.cn id=324 lang=python3
#
# [324] 摆动排序 II
#
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        # 降序
        nums.sort(reverse=True)
        nums[1::2], nums[0::2] = nums[:len(nums) // 2], nums[len(nums) // 2:]

