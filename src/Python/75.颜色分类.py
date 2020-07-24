#
# @lc app=leetcode.cn id=75 lang=python3
#
# [75] 颜色分类
#
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        # 计数排序
        count = [0,0,0]
        for num in nums:
            count[num] += 1
        idx = 0
        for i in range(3):
            for j in range(count[i]):
                nums[idx] = i
                idx += 1


