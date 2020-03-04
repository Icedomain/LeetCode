#
# @lc app=leetcode.cn id=349 lang=python3
#
# [349] 两个数组的交集
#
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))

