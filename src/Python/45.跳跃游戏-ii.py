#
# @lc app=leetcode.cn id=45 lang=python3
#
# [45] 跳跃游戏 II
#
class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0
        # (start -> end )
        end = nums[0]
        start = 0
        step = 1
        maxDis = nums[0]
        while end < len(nums) - 1:
            # 看一步最远能走到哪
            for i in range(start + 1, end + 1):
                maxDis = max(maxDis, nums[i] + i)
            start = end
            end = maxDis
            step += 1
        return step
