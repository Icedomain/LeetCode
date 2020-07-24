#
# @lc app=leetcode.cn id=88 lang=python3
#
# [88] 合并两个有序数组
#
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # 从后往前
        p1 = m - 1
        p2 = n - 1
        p = m + n -1
        # 两个都没放完
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] >= nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1
        # p1没放完，那就不用再操作了
        # p2没放完
        while p2 >= 0:
            nums1[p] = nums2[p2]
            p -= 1
            p2 -= 1


